
let copyPasta = ["不好意思打斷你。你所說的Linux，事實是上GNU/Linux，或者我習慣叫他GNU+Linux。Linux本身並不是一個作業系統，而是功能齊全的GNU系統其中的一個自由組件，shell和其他重要的系統組件靠POSIX構成了完整作業系統...",
  " Many computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called Linux, and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.",
  "There really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called Linux distributions are really distributions of GNU/Linux! ",
  "高中想先讀微積分，大學想修好微積分？唯一推薦Rudin寫的《Principle of mathematical analysis》，這本書輕、薄、短、小，是數學系愛用的名著。微積分的書往往很大一本，又重又厚，對剛接觸微積分的人來說，常感到相當震撼而放棄學習。Rudin寫書最大的特色就是兩個字：簡潔。他寫書的功力之強大，別人需要很大的篇幅處理的，他幾筆就帶過了，適合對英文有障礙的人，能馬上看到重點，廢話不多。",
  "如果你覺得我說的話不可信，那看看臺大數學系的書評吧：「這本書不論是自修、教學，都很適合。是本很好的書。」「與其說這是一本教科書，不如說這是一本字典。」由此可見，這本書適合自己讀，內容豐富，常被數學系拿來使用，也就不意外了。事實上這本書還有一個暱稱：Baby rudin，可想而知，它相當平易近人。",
  "大致來看裡面的內容，第一章先幫你複習什麼是實數(你看，像不像回到國小)，第二章來點有趣的拓樸， 像是距離、連通一些基本概念，讓你重拾對數學的興趣。第三章先講數列的收斂，第四章談連續性，一直在複習高中的內容，怕你沒有聽選修數學。直到第五、六章，才正式進入微分和積分，後面都是有趣的題材，像第八章告訴你幾個特殊函數，在一些問題上能應用這些技巧，第九章講多變數函數，順便複習線性代數。第十章是幾何的內容，這在微積分的書很少見，可以參考參考。總之，這是一本內容豐富的好書，真心不私藏，在這邊推薦給大家。",
  "SAYING: 1.你們第一次做看學長的，學長也第一次做。這樣是盲人引導盲人  2.有一種學習方式是先知道怎麼用之後，再知道背後的原理  3.任何物件導向的問題，都可以透過增加一層中介層來解決；當然，除了中介層過多的這個問題 4.老鷹首先用牠的喙擊打岩石，直到完全脫落再找到eigencalue 5.鯉魚王是甚麼魚 6.W      ork -Alen Turing  7.Welcome to Jenkins! Invalid username or password.",
];
let jeLongIp = ''
function send() {
  console.log("send")
  let text = document.querySelector("#input").value
  if (text === '') {

  } else if (text[0] === '!') {
    if (text.split(' ')[0] === '!set') {
      jeLongIp = text.split(' ')[1]
      document.querySelector("#input").value = ''

      let data1 = {
        "name": "newjeLong",
        "text": "connect to " + jeLongIp,
      }
      console.log(data1)
      let xhr1 = new XMLHttpRequest()
      xhr1.open("POST", "/post")
      xhr1.setRequestHeader('Content-type', 'application/json');
      xhr1.send(JSON.stringify(data1))
      document.querySelector("#input").value = ''
    } else if (text.split(' ')[0] === '!new' && text.split(' ').length === 3) {
      let tmp = text.split(' ')
      let data = {
        "name": tmp[1],
        "rule_type": 'jsp'
      }
      let xhr = new XMLHttpRequest()
      xhr.open("POST", 'http://' + jeLongIp + "/threads/")
      xhr.setRequestHeader('Content-type', 'application/json');
      xhr.send(JSON.stringify(data))
      document.querySelector("#input").value = ''

      let data1 = {
        "name": "newjeLong",
        "text": tmp[2],
      }
      console.log(data1)
      let xhr1 = new XMLHttpRequest()
      xhr1.open("POST", "/post")
      xhr1.setRequestHeader('Content-type', 'application/json');
      xhr1.send(JSON.stringify(data1))
      document.querySelector("#input").value = ''

    } else if (text.split(' ')[0] === '!get') {
      document.querySelector("#input").value = ''
      if (text.split(' ').length === 1) {

        let xhr = new XMLHttpRequest()
        xhr.open("GET", 'http://' + jeLongIp + "/threads", true)
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.setRequestHeader('Access-Control-Allow-Origin', 'http://' + jeLongIp);
        xhr['Access-Control-Allow-Origin'] = 'http://' + jeLongIp;
        xhr.send()
        xhr.onload = () => {
          let data = JSON.parse(xhr.response)
          data.forEach(element => {
            let data1 = {
              "name": 'jelong',
              "text": element['data'],
            }
            console.log(data1)
            let xhr1 = new XMLHttpRequest()
            xhr1.open("POST", "/post")
            xhr1.setRequestHeader('Content-type', 'application/json');
            xhr1.send(JSON.stringify(data1))
            document.querySelector("#input").value = ''

          });
        }
      } else {
        let tmp = text.split(' ')[1]
        let xhr = new XMLHttpRequest()
        xhr.open("GET", 'http://' + jeLongIp + "/threads/" + tmp)
        xhr.send()
        xhr.onload = () => {
          console.log("update scuss")
          let data = JSON.parse(xhr.response)
          console.log(data)
          let data1 = {
            "name": "newjeLong",
            "text": data['data'],
          }
          console.log(data1)
          let xhr1 = new XMLHttpRequest()
          xhr1.open("POST", "/post")
          xhr1.setRequestHeader('Content-type', 'application/json');
          xhr1.send(JSON.stringify(data1))
          document.querySelector("#input").value = ''
        }
      }



    } else if (text.split(' ')[0] === '!je') {
      document.querySelector("#input").value = ''
      let longId = text.split(' ')[1]
      let continuw_word = text.split(' ')[2]

      let data = {
        "continue_word": continuw_word
      }
      let xhr = new XMLHttpRequest()
      xhr.open("POST", 'http://' + jeLongIp + "/threads/" + longId + '/continue')
      xhr.setRequestHeader('Content-type', 'application/json');
      xhr.send(JSON.stringify(data))
      xhr.onload = () => {
        console.log("update scuss")
        let data = JSON.parse(xhr.response)
        console.log(data)
        let data1 = {
          "name": "newjeLong",
          "text": data['message'],
        }
        console.log(data1)
        let xhr1 = new XMLHttpRequest()
        xhr1.open("POST", "/post")
        xhr1.setRequestHeader('Content-type', 'application/json');
        xhr1.send(JSON.stringify(data1))


      }




    } else if (text.split(' ')[0] === '!h1') {
      let data = {
        "name": "jeLong",
        "text": '!get all long; !get {longname} ;!je {longname} {word}',
      }
      console.log(data)
      let xhr = new XMLHttpRequest()
      xhr.open("POST", "/post")
      xhr.setRequestHeader('Content-type', 'application/json');
      xhr.send(JSON.stringify(data))
      document.querySelector("#input").value = ''

    } else {
      let data = {
        "name": "jeLong",
        "text": '!set {ip:port}to set serverip; !new {longname} {rule} to set newlong; !h1 :to get other help',
      }
      console.log(data)
      let xhr = new XMLHttpRequest()
      xhr.open("POST", "/post")
      xhr.setRequestHeader('Content-type', 'application/json');
      xhr.send(JSON.stringify(data))
      document.querySelector("#input").value = ''


    }



  } else {
    let data = {
      "name": "client1",
      "text": text,
    }
    console.log(data)
    let xhr = new XMLHttpRequest()
    xhr.open("POST", "/post")
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.send(JSON.stringify(data))
    document.querySelector("#input").value = ''
  }
}
function update() {
  let xhr = new XMLHttpRequest()
  xhr.open("GET", "/get")
  xhr.send()
  xhr.onload = () => {
    console.log("update scuss")
    let data = JSON.parse(xhr.response)
    console.log(data)
    let block = document.querySelector("#context")
    block.innerHTML = ""
    let copyPastaIndex = 0;

    data = data["_default"]
    for (const key in data) {
      let element = data[key];
      if (copyPastaIndex >= copyPasta.length) {
        copyPastaIndex = 0;
      }

      buf = ''
      for (const key1 in element) {
        if (key1 == 'content') {
          block.innerHTML = "<li ><a href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'> " + "<h3>" + element[key1] + buf + block.innerHTML;
        }
        else if (key1 == 'user') {
          buf += " -user" + element[key1] + "</h3></a>" + "</li > ";
          buf += '<li class="text">' + copyPasta[copyPastaIndex] + '</li>'
          copyPastaIndex += 1;
        }

      }
    }
  };

}
document.querySelector("#submit").addEventListener("click", send)
setInterval(update, 200);