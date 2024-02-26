const avail_section = document.getElementById('availsection')
const C_A_btn = document.getElementById('C_A_btn')
const pay_btn = document.getElementById('pay_btn')
const date_selector = document.getElementById('date_selector')

C_A_btn.addEventListener('click', () => {
    const from_date = document.getElementById('date_F').value;
    const to_date = document.getElementById('date_T').value;
    const venue_cat = document.getElementById('V_cat').value;
    const venue_name = document.getElementById('V_name').value;
    const url = `/check_availablity/${from_date}/${to_date}/${venue_cat}/${venue_name}/`;
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.available) {
                avail_section.innerHTML = ''
                avail_section.innerHTML = 'Available'

                var options = {
                    key: `${data.context.razorpay_merchant_key}`,
                    amount: `${data.context.order.amount}`,
                    currency: `${data.context.order.currency}`,
                    name: "Locations",
                    order_id: `${data.context.order.id}`,
                    callback_url: `${data.context.callback_url}`
                }

                var rzp1 = new Razorpay(options);
                pay_btn.disabled = false
                pay_btn.style.backgroundColor = 'red'
                pay_btn.onclick = (e) => {
                    rzp1.open();
                    e.preventDefault();
                }
            } else if (data?.redirect){
                window.location.href = data.redirect
            } else {
                avail_section.innerHTML = ''
                avail_section.innerHTML = 'Not Available'
            }
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });

})
