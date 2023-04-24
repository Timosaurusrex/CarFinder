
/*
import { launch } from 'puppeteer';

async function getQuotes(){
    // Start a Puppeteer session with:
    // - a visible browser (`headless: false` - easier to debug because you'll see the browser in action)
    // - no default viewport (`defaultViewport: null` - website page will be in full width and height)
    const browser = await launch({
        headless: false,
        defaultViewport: null,
    });

    // Open a new page
    const page = await browser.newPage();
    await page.goto("https://www.willhaben.at/iad/gebrauchtwagen/auto/gebrauchtwagenboerse?sfId=b82af512-8a99-419e-a408-df37680ae11d&isNavigation=true&CAR_MODEL/MAKE=1065&CAR_MODEL/MODEL=1691&rows=30&keyword=Variant&EQUIPMENT=15&ENGINE/FUEL=100003&page=1&MILEAGE_TO=90000&YEAR_MODEL_FROM=2018&PRICE_TO=21000&ENGINEEFFECT_FROM=74", {
        waitUntil: "domcontentloaded",
    });
    const quotes = await page.evaluate(() => {
        // Fetch the first element with class "quote"
        // Get the displayed text and returns it
        const quoteList = document.querySelectorAll(".Box-sc-wfmb7k-0 iENLOS");

        // Convert the quoteList to an iterable array
        // For each quote fetch the text and author
        return Array.from(quoteList).map((quote) => {
        // Fetch the sub-elements from the previously fetched quote element
        // Get the displayed text and return it (`.innerText`)
        const auto = quote.querySelector(".Text-sc-10o2fdq-0 fFalrS").innerText;
        const preis = quote.querySelector(".Text-sc-10o2fdq-0 duCArz").innerText;

        return { auto, preis };
        });
    });

    // Display the quotes
    console.log(quotes);

    // Close the browser
    await browser.close();
};
*/

function filter(){
    send = false;
    brand = document.getElementById("brand");
    type = document.getElementById("type");
    keyword = document.getElementById("keyword");
    mileage = document.getElementById("mileage");
    price = document.getElementById("price");
    year = document.getElementById("year");
    power = document.getElementById("power");
    heatedSeats = document.getElementById("heated_seats");
    navigation = document.getElementById("navigation");
    diesel = document.getElementById("diesel");
    hybrid = document.getElementById("hybrid");
    benzin = document.getElementById("benzin");
    elektro = document.getElementById("elektro");
    updateButton = document.getElementById('update-button');

    const filter = {
        brand: brand.value,
        type: type.value,
        keyword: keyword.value,
        mileage: mileage.value,
        price: price.value,
        year: year.value,
        extras: {
        heatedSeats: heatedSeats.checked,
        navigation: navigation.checked,
        diesel: diesel.checked,
        benzin: benzin.checked,
        elektro: elektro.checked,
        hybrid: hybrid.checked
        }
    };

    console.log(filter);
    const box = document.querySelector(".box");
    text = JSON.stringify(filter);
    box.innerText = text;
}

function copyFunction() {
var copyText,
element = document.getElementById("box");
console.log(element);
if (element != null) {
  copyText = element.innerText;
  console.log(copyText);
  navigator.clipboard.writeText(copyText);
}
else {
  copyText = null;
}
}


function renderCars() {
    const carsJson = document.getElementById("json-input").value;

    const cars34 = carsJson.replaceAll("'", "<%>");
    const data = cars34.replaceAll("<%>", '"');

    const cars = JSON.parse(data);
    console.log(cars);
    
    const autos = cars.Autos;
    const imageContainer = document.querySelector('.scrollable-images');
    
    autos.forEach(auto => {
      if (auto.url && auto.image && auto.price && auto.km && auto.ez) {
        const autoDiv = document.createElement('div');
        autoDiv.className = 'auto';
        const autoImage = document.createElement('img');
        autoImage.src = auto.image;
        autoImage.onclick = () => {
        window.open(auto.url, "_blank");
        };
        const autoDetails = document.createElement('div');
        autoDetails.className = 'details';
        const autoPrice = document.createElement('p');
        autoPrice.innerHTML = `Price: ${auto.price}`;
        const autoKm = document.createElement('p');
        autoKm.innerHTML = `km: ${auto.km}`;
        const autoEz = document.createElement('p');
        autoEz.innerHTML = `ez: ${auto.ez}`;
    
        autoDiv.appendChild(autoImage);
        autoDiv.appendChild(autoDetails);
        autoDetails.appendChild(autoPrice);
        autoDetails.appendChild(autoKm);
        autoDetails.appendChild(autoEz);
    
        imageContainer.appendChild(autoDiv);
      }
    });
  }





    


