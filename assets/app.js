new Vue({
    el: '#vue-app',
    delimiters: ['${', '}'],
    data: {
        working: true,
        close: true,
        buttonMsg: 'business open now'
    },
    methods: {
        changeButton: function(){
            if (this.working == true){
                this.working = false;
                this.buttonMsg = "business close now"
            } else{
                this.working = true;
                this.buttonMsg = "business open now"
            }
        }
    }
})