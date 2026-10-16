const productDataset = [
    { "id": 1, "name": "Tahu kocek original", "category": "Makanan", "price": 10000, "stock": 24 },
    { "id": 2, "name": "Tahu kocek sosis", "category": "Makanan", "price": 10000, "stock": 27 },
    { "id": 3, "name": "Tahu kocek tempura", "category": "Makanan", "price": 10000, "stock": 21 },
    { "id": 4, "name": "Tahu kocek sosis mix tempura", "category": "Makanan", "price": 15000, "stock": 23 },
    { "id": 5, "name": "Tahu kocek basreng", "category": "Makanan", "price": 10000, "stock": 22 },
    { "id": 6, "name": "Tahu kocek tempura mix basreng", "category": "Makanan", "price": 15000, "stock": 26 },
    { "id": 7, "name": "Tahu kocek basreng mix sosis", "category": "Makanan", "price": 15000, "stock": 25 },
    { "id": 8, "name": "Tahu kocek cireng", "category": "Makanan", "price": 15000, "stock": 29 }
];

const formatRupiah = (number) => {
    return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR' }).format(number);
};

document.addEventListener('DOMContentLoaded', () => {
    // Mengambil elemen berdasarkan ID dari HTML-mu yang sederhana tadi
    const form = document.getElementById('productForm');
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
        event.preventDefault(); // Mencegah reload halaman

        const nameVal = nameInput.value.trim();
        const catVal = categoryInput.value;
        const priceVal = parseFloat(priceInput.value);
        const stockVal = parseInt(stockInput.value);

        if (!nameVal || !catVal || isNaN(priceVal) || priceVal <= 0 || isNaN(stockVal) || stockVal < 0) {
            feedback.textContent = "Mohon isi semua data produk dengan valid!";
            feedback.style.color = "red";
            feedback.style.display = "block";
            return;
        }

        const newProduct = {
            id: productDataset.length + 1,
            name: nameVal,
            category: catVal,
            price: priceVal,
            stock: stockVal
        };

        productDataset.push(newProduct);

        console.log("Data produk berhasil ditambahkan:", newProduct);
        console.log("Total Dataset Sekarang:", productDataset);

        feedback.textContent = `Sukses! Produk '${newProduct.name}' (${formatRupiah(newProduct.price)}) tersimpan.`;
        feedback.style.color = "green";
        feedback.style.display = "block";

        form.reset();
        livePreviewText.textContent = "";

        setTimeout(() => {
            feedback.style.display = "none";
        }, 3000);
    });
});