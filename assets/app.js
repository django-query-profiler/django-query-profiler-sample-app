var app2 = new Vue({
    el: "#vue-prepare",
    delimiters: ['${', '}'],
    data: {
        msg: 'test',
        orders: [],
        loading: false,
        currentOrder: {},
        message: null,
        newOrder: { 'article_heading': null, 'article_body': null },
      },
    mounted: function() {
        this.getOrders();
    },
    methods: {
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
              this.$http.get(`/food/orderdetail/${id}`)
                .then((response) => {
                    this.currentOrder = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
          },
          deleteOrder: function(id) {
            this.loading = true;
            this.$http.delete(`/food/orderdetail/${id}/`)
                .then((response) => {
                    this.loading = false;
                    this.getOrders();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
          }
      }
})