var app2 = new Vue({
    el: "#vue-prepare",
    delimiters: ['${', '}'],
    data: {
        orders: [],
        business_open: '',
        loading: false,
        currentOrder: {},
        message: null,
        newOrder: { 'name': null, 'coffee_order': null },
      },
    mounted: function() {
        this.getOrders();
        this.getBusinessStatus();
    },
    methods: {
        getCookie: function(name) {
            var value = '; ' + document.cookie
            var parts = value.split('; ' + name + '=')
            if (parts.length === 2) return parts.pop().split(';').shift()
        },
        getOrders: function() {
            this.loading = true;
            this.$http.get('/food/orderlist/')
                .then((response) => {
                    this.orders = response.data;
                    this.loading = false;
                    })
                .catch ((err) => {
                    this.loading = false;
                    console.log(err);
                })
          },
          getOrder: function(id) {
              this.loading = true;
              this.$http.get(`/food/orderdetail/${id}/`)
                .then((response) => {
                    this.currentOrder = response.data;
                    $("#editOrderModal").modal('show');
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
          },
          deleteOrder: function(id) {
            this.loading = true;
            this.$http.delete(`/food/orderdetail/${id}/`, {headers: {'X-CSRFToken': this.getCookie('csrftoken')}} )
                .then((response) => {
                    this.loading = false;
                    this.getOrders();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
          },
          updateOrder: function() {
              this.loading = true;
              this.$http.put(`/food/orderdetail/${this.currentOrder.id}/`, this.currentOrder, {headers: {'X-CSRFToken': this.getCookie('csrftoken')}} )
                .then((response) => {
                    this.loading = false;
                    this.currentOrder = response.data;
                    this.getOrders();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
          },
          getBusinessStatus: function() {
              this.$http.get('/food/business')
                .then((response) => {
                    this.business_open = ($(response.data).find('#business_status').text() == 'open');
                })
                .catch((err) => {
                    console.log(err);
                })
          }
      }
})

setInterval(async function() {
    let response = await fetch('/food/orderlist/');
    let data = await response.json();
    app2.loading = true;
    app2.orders = data;
    app2.loading = false;

    app2.getBusinessStatus();
}, 7000)
