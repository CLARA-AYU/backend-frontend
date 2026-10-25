const defaultData = [
    { "id": 1, "name": "Tahu kocek original", "category": "Makanan", "price": 10000, "stock": 24 },
    { "id": 2, "name": "Tahu kocek sosis", "category": "Makanan", "price": 10000, "stock": 27 },
    { "id": 3, "name": "Tahu kocek tempura", "category": "Makanan", "price": 10000, "stock": 21 },
    { "id": 4, "name": "Tahu kocek sosis mix tempura", "category": "Makanan", "price": 15000, "stock": 23 },
    { "id": 5, "name": "Tahu kocek basreng", "category": "Makanan", "price": 10000, "stock": 22 },
    { "id": 6, "name": "Tahu kocek tempura mix basreng", "category": "Makanan", "price": 15000, "stock": 26 },
    { "id": 7, "name": "Tahu kocek basreng mix sosis", "category": "Makanan", "price": 15000, "stock": 25 },
    { "id": 8, "name": "Tahu kocek cireng", "category": "Makanan", "price": 15000, "stock": 29 }
];

let productDataset = JSON.parse(localStorage.getItem('dataProdukUMKM'));

if (!productDataset || productDataset.length === 0) {
    productDataset = [...defaultData]; 
    localStorage.setItem('dataProdukUMKM', JSON.stringify(productDataset)); 
}

const simpanData = () => {
    localStorage.setItem('dataProdukUMKM', JSON.stringify(productDataset));
};
const formatRupiah = (number) => {
    return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR' }).format(number);
};

const renderProductCards = (products) => {
    const container = document.querySelector('#product-container');
    if (!container) return;
    container.innerHTML = ''; 
    products.forEach((prod) => {
        const card = document.createElement('article');
        card.className = 'product-card dynamic-item';
        card.setAttribute('data-id', prod.id);
        card.innerHTML = `
            <h3 class="product-title">${prod.name}</h3>
            <p class="product-category">${prod.category}</p>
            <p class="product-price">${formatRupiah(prod.price)}</p>
            <p class="product-stock">Sisa Stok: <span class="badge">${prod.stock}</span></p>
        `;
        container.append(card);
    });
};

const renderProductTable = (products) => {
    const tbody = document.querySelector('#table-body');
    if (!tbody) return;
    tbody.innerHTML = '';
    products.forEach((prod) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${prod.id}</td>
            <td>${prod.name}</td>
            <td>${prod.category}</td>
            <td>${formatRupiah(prod.price)}</td>
            <td>${prod.stock}</td>
            <td>
                <button class="btn btn-edit" onclick="handleEditProduct(${prod.id})">Edit</button>
                <button class="btn btn-delete" onclick="handleDeleteProduct(${prod.id})">Hapus</button>
            </td>
        `;
        tbody.append(tr);
    });
};

window.handleDeleteProduct = (productId) => {
    if(confirm("Yakin ingin menghapus produk ini?")) {
        productDataset = productDataset.filter(prod => prod.id !== productId);
        simpanData();
        renderProductCards(productDataset);
        renderProductTable(productDataset);
        console.log(`[HAPUS DATA] Produk dengan ID ${productId} berhasil dihapus secara permanen.`);
    }
};

window.handleEditProduct = (productId) => {
    const prod = productDataset.find(p => p.id == productId); 
    if (prod) {

        document.getElementById('editModeId').value = prod.id;
        document.getElementById('name').value = prod.name;
        document.getElementById('category').value = prod.category;
        document.getElementById('price').value = prod.price;
        document.getElementById('stock').value = prod.stock;

        document.getElementById('formTitle').innerText = "Edit Data Produk";
        document.getElementById('btnSubmit').innerText = "Update Produk";
        document.getElementById('btnSubmit').style.backgroundColor = "#e3d5ca"; 
        document.getElementById('btnSubmit').style.color = "#7a6b58";
        
        document.getElementById('btnCancelEdit').style.display = 'block';

        document.getElementById('productForm').scrollIntoView({ behavior: 'smooth' });
        console.log("[TAMBAH DATA] Produk baru berhasil ditambahkan ke sistem:", newProduct);
    }
};

window.batalEdit = () => {
    document.getElementById('productForm').reset();
    document.getElementById('editModeId').value = ""; 
 
    document.getElementById('formTitle').innerText = "Tambah Produk Baru";
    document.getElementById('btnSubmit').innerText = "Simpan Produk";
    document.getElementById('btnSubmit').style.backgroundColor = "#d4a5a5"; 
    document.getElementById('btnSubmit').style.color = "white";
    
    document.getElementById('btnCancelEdit').style.display = 'none';
    document.getElementById('livePreviewText').textContent = "(Ketik di form untuk melihat preview...)";
};

document.addEventListener('DOMContentLoaded', () => {
    renderProductCards(productDataset);
    renderProductTable(productDataset);

    const form = document.getElementById('productForm');
    if (form) { 
        const feedback = document.getElementById('feedbackMessage');
        const livePreviewText = document.getElementById('livePreviewText');
        const nameInput = document.getElementById('name');
        const categoryInput = document.getElementById('category');
        const priceInput = document.getElementById('price');
        const stockInput = document.getElementById('stock');

        form.addEventListener('input', () => {
            const nameStr = nameInput.value || '';
            const catStr = categoryInput.value || '';
            const priceStr = priceInput.value ? formatRupiah(priceInput.value) : '';
            const stockStr = stockInput.value ? `(${stockInput.value} pcs)` : '';
            livePreviewText.textContent = `${nameStr} ${catStr} ${priceStr} ${stockStr}`;
        });

        form.addEventListener('submit', (event) => {
            event.preventDefault(); 
            const nameVal = nameInput.value.trim();
            const catVal = categoryInput.value;
            const priceVal = parseFloat(priceInput.value);
            const stockVal = parseInt(stockInput.value);

            if (!nameVal || !catVal || isNaN(priceVal) || priceVal <= 0 || isNaN(stockVal) || stockVal < 0) {
                feedback.textContent = "Mohon isi semua data produk dengan valid!";
                feedback.style.color = "#c98a8a"; 
                feedback.style.display = "block";
                return;
            }

            const editId = document.getElementById('editModeId').value;

            if (editId !== "") {
                const index = productDataset.findIndex(p => p.id == editId);
                
                if(index !== -1) {
                    productDataset[index].name = nameVal;
               
                    console.log(`[EDIT DATA] Produk ID ${editId} berhasil diubah menjadi:`, productDataset[index]);
                }
           } else {

                const newId = productDataset.length > 0 ? Math.max(...productDataset.map(p => p.id)) + 1 : 1;
   
                const newProduct = { id: newId, name: nameVal, category: catVal, price: priceVal, stock: stockVal };
                
                productDataset.push(newProduct);
           
                console.log("[TAMBAH DATA] Produk baru berhasil ditambahkan ke sistem:", newProduct);
            }

            simpanData(); 
            renderProductTable(productDataset);
            
            feedback.style.color = "#8db596"; // Hijau soft
            feedback.style.display = "block";

            // Selesai submit, reset form ke kondisi normal (mode tambah)
            batalEdit();
            
            setTimeout(() => { feedback.style.display = "none"; }, 3000);
        });
    }
});