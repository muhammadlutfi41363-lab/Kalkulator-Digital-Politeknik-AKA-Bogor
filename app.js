// TAB MENU

function openTab(id){
  let tabs = document.querySelectorAll(".tab-content");
  tabs.forEach(tab => {
    tab.classList.remove("active");
  });
  document.getElementById(id).classList.add("active");
}

openTab("larutan");

// SIMPAN RIWAYAT

function simpanRiwayat(data){
  let riwayat = JSON.parse(localStorage.getItem("riwayat")) || [];
  riwayat.push(data);
  localStorage.setItem("riwayat", JSON.stringify(riwayat));
  tampilkanRiwayat();
}

// TAMPILKAN RIWAYAT

function tampilkanRiwayat(){
  let list = document.getElementById("listRiwayat");
  if(!list) return;
  let riwayat = JSON.parse(localStorage.getItem("riwayat")) || [];
  list.innerHTML = "";
  
  riwayat.slice().reverse().forEach(item => {
    // Hapus tag HTML untuk tampilan bersih di riwayat
    let teksBersih = item.replace(/<[^>]*>/g, '');
    list.innerHTML += `<div class="riwayat-item">${teksBersih}</div>`;
  });
}

tampilkanRiwayat();

// HAPUS RIWAYAT

function hapusRiwayat(){
  if(confirm("Yakin ingin menghapus semua riwayat?")){
    localStorage.removeItem("riwayat");
    tampilkanRiwayat();
  }
}

// PEMBUATAN LARUTAN

function hitungLarutan(){
  let mr = parseFloat(document.getElementById("mr").value);
  let volume = parseFloat(document.getElementById("volume").value);
  let molaritas = parseFloat(document.getElementById("molaritas").value);
  
  if(isNaN(mr) || isNaN(volume) || isNaN(molaritas)){
    alert("Isi semua data!");
    return;
  }
  
  if(mr <= 0){
    alert("Massa molar (Mr) harus lebih dari 0!");
    return;
  }
  
  if(volume <= 0){
    alert("Volume harus lebih dari 0 mL!");
    return;
  }
  
  if(molaritas <= 0){
    alert("Konsentrasi (M) harus lebih dari 0!");
    return;
  }
  
  let massa = molaritas * (volume/1000) * mr;
  let hasil = `Massa yang dibutuhkan: ${massa.toFixed(4)} gram`;
  
  document.getElementById("hasilLarutan").innerHTML = hasil;
  simpanRiwayat("Larutan → " + hasil);
}

// PENGENCERAN - Hitung V2

function hitungV2(){
  let m1 = parseFloat(document.getElementById("m1").value);
  let v1 = parseFloat(document.getElementById("v1").value);
  let m2 = parseFloat(document.getElementById("m2").value);
  
  if(isNaN(m1) || isNaN(v1) || isNaN(m2)){
    alert("Isi semua data!");
    return;
  }
  
  if(m1 <= 0 || v1 <= 0 || m2 <= 0){
    alert("Nilai harus lebih dari 0!");
    return;
  }
  
  let v2 = (m1 * v1) / m2;
  let hasil = `Volume Akhir (V₂) = <b>${v2.toFixed(2)} mL</b>`;
  
  document.getElementById("hasilV2").innerHTML = hasil;
  simpanRiwayat(`Pengenceran → V₂ = ${v2.toFixed(2)} mL`);
}

// PENGENCERAN - Hitung V1

function hitungV1(){
  let m1 = parseFloat(document.getElementById("m1_v1").value);
  let m2 = parseFloat(document.getElementById("m2_v1").value);
  let v2 = parseFloat(document.getElementById("v2_v1").value);
  
  if(isNaN(m1) || isNaN(m2) || isNaN(v2)){
    alert("Isi semua data!");
    return;
  }
  
  if(m1 <= 0 || m2 <= 0 || v2 <= 0){
    alert("Nilai harus lebih dari 0!");
    return;
  }
  
  let v1 = (m2 * v2) / m1;
  let hasil = `Volume Awal (V₁) = <b>${v1.toFixed(2)} mL</b>`;
  
  document.getElementById("hasilV1").innerHTML = hasil;
  simpanRiwayat(`Pengenceran → V₁ = ${v1.toFixed(2)} mL`);
}

// TABEL PERIODIK (DIPERBAIKI)

function tampilkanPeriodik(){
  let container = document.getElementById("periodicTable");
  if(!container) return;
  container.innerHTML = "";
  
  for(let simbol in unsur){
    // Pastikan unsur[simbol] adalah objek dengan properti nomor dan massa
    let nomorAtom = unsur[simbol].nomor || "?";
    let massaAtom = unsur[simbol].massa || "?";
    
    container.innerHTML += `
      <div class="unsur-box">
        <h3>${simbol}</h3>
        <p>${nomorAtom}</p>
        <small>${massaAtom} g/mol</small>
      </div>
    `;
  }
}

tampilkanPeriodik();

// FUNGSI RESET FORM (TAMBAHAN - OPSIONAL)

function resetFormLarutan(){
  document.getElementById("mr").value = "";
  document.getElementById("volume").value = "";
  document.getElementById("molaritas").value = "";
  document.getElementById("hasilLarutan").innerHTML = "";
}

function resetFormPengenceran(){
  document.getElementById("m1").value = "";
  document.getElementById("v1").value = "";
  document.getElementById("m2").value = "";
  document.getElementById("hasilV2").innerHTML = "";
  document.getElementById("m1_v1").value = "";
  document.getElementById("m2_v1").value = "";
  document.getElementById("v2_v1").value = "";
  document.getElementById("hasilV1").innerHTML = "";
}