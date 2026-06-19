const outputBox=document.getElementById("outputBox");
const taskInput=document.getElementById("taskInput");
const modeSelect=document.getElementById("modeSelect");
const runButton=document.getElementById("runButton");
const copyButton=document.getElementById("copyButton");
const installButton=document.getElementById("installButton");
let deferredPrompt=null;
if("serviceWorker" in navigator){navigator.serviceWorker.register("./service-worker.js").catch(console.error)}
window.addEventListener("beforeinstallprompt",e=>{e.preventDefault();deferredPrompt=e;installButton.hidden=false});
installButton.addEventListener("click",async()=>{if(!deferredPrompt)return;deferredPrompt.prompt();await deferredPrompt.userChoice;deferredPrompt=null;installButton.hidden=true});
copyButton.addEventListener("click",async()=>{await navigator.clipboard.writeText(outputBox.textContent||"");copyButton.textContent="Copied";setTimeout(()=>copyButton.textContent="Copy",1200)});
runButton.addEventListener("click",async()=>{
  const input=taskInput.value.trim();
  if(!input){outputBox.textContent="Masukkan link YouTube, transkrip, Pine Script, atau catatan strategi terlebih dahulu.";return}
  const proxyUrl=window.AGENT_CONFIG?.proxyUrl;
  if(!proxyUrl||proxyUrl.includes("YOUR-BACKEND-DOMAIN")){
    outputBox.textContent=["Backend proxy belum disetting.","","Edit file:","web-app/src/agent-config.js","","Ganti proxyUrl ke URL backend kamu."].join("\n");return
  }
  runButton.disabled=true;
  outputBox.textContent="Agent sedang bekerja...\n\nResearch → Logic → Risk Review → Repaint Audit → Final Committee";
  try{
    const response=await fetch(proxyUrl,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({input,mode:modeSelect.value,app:window.AGENT_CONFIG})});
    const text=await response.text();
    let data;try{data=JSON.parse(text)}catch{data={report:text}}
    outputBox.textContent=response.ok?(data.report||JSON.stringify(data,null,2)):`Backend error ${response.status}:\n\n${JSON.stringify(data,null,2)}`;
  }catch(error){
    outputBox.textContent=["Gagal menghubungi backend.","","Cek URL backend, CORS, server aktif, dan internet.","",String(error.message||error)].join("\n");
  }finally{runButton.disabled=false}
});
