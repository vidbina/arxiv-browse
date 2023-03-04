"""Example of a listing service for testing."""

# pylint: skip-file

import datetime
from typing import List, Optional

from browse.services.listing import MonthCount

from . import (Listing, ListingCountResponse, ListingItem, ListingNew,
               ListingService)


class FakeListingFilesService(ListingService):
    """Listing service used for development and testing purposes.

    This is intended as an example of what the /listing controller
    needs for methods from a listing service.

    This just returns examples that should be good enough. This makes
    no attempt to return the correct articles for a date or the correct
    primaries for articles.
    """

    @classmethod
    def version(cls) -> str:
        """Version."""
        return f"0.{__file__}"

    def monthly_counts(self, archive: str, year: int) -> ListingCountResponse:
        """Example of monthly_counts."""
        counts = [
            MonthCount(year, 1, 1234, 234, '', []),
            MonthCount(year, 2, 1224, 134, '', []),
            MonthCount(year, 3, 1334, 324, '', []),
            MonthCount(year, 4, 1534, 134, '', []),
            MonthCount(year, 5, 1644, 234, '', []),
            MonthCount(year, 6, 983, 314, '', []),
            MonthCount(year, 7, 876, 132, '', []),
            MonthCount(year, 8, 1233, 294, '', []),
            MonthCount(year, 9, 1453, 273, '', []),
            MonthCount(year, 10, 1502, 120, '', []),
            MonthCount(year, 11, 1638, 100, '', []),
            MonthCount(year, 12, 1601, 233, '', []),
        ]
        return ListingCountResponse(
            month_counts= counts,
            new_count= sum([mm.new for mm in counts]),
            cross_count= sum([mm.cross for mm in counts]))


    def list_new_articles(
        self,
        archiveOrCategory: str,
        skip: int,
        show: int,
        if_modified_since: Optional[str] = None,
    ) -> ListingNew:
        """Example of list_new_articles."""
        listings = [
            "0704.0526",
            "0704.0988",
            "0704.0182",
            "0704.0310",
            "0704.0616",
            "0704.0732",
            "0704.0042",
            "0704.0615",
            "0704.0568",
            "0704.0319",
            "0704.0265",
            "0704.0133",
            "0704.0533",
            "0704.0453",
            "0704.0276",
            "0704.0991",
            "0704.0740",
            "0704.0473",
            "0704.0083",
            "0704.0278",
            "0704.0006",
            "0704.0735",
            "0704.0753",
            "0704.0324",
            "0704.0600",
            "0704.0737",
            "0704.0387",
            "0704.0659",
            "0704.0432",
            "0704.0408",
            "0704.0895",
            "0704.0088",
            "0704.0719",
            "0704.0124",
            "0704.0508",
        ]
        items2 = [ListingItem(id, "new", "cs.DB") for id in listings]
        items3 = [
            ListingItem("0704.0074", "cross", "cs.DL"),
            ListingItem("0704.0075", "cross", "cs.GT"),
            ListingItem("0704.0333", "cross", "cs.NA"),
            ListingItem("0704.0445", "cross", "cs.NE"),
            ListingItem("0704.0226", "cross", "cs.NA"),
            ListingItem("0704.0266", "cross", "cs.GT"),
            ListingItem("0704.0368", "cross", "cs.CV"),
            ListingItem("0704.0716", "cross", "cs.DL"),
            ListingItem("0704.0373", "cross", "cs.DL"),
            ListingItem("0704.0378", "cross", "cs.CV"),
            ListingItem("0704.0536", "cross", "cs.DL"),
            ListingItem("0704.0239", "cross", "cs.DL"),
            ListingItem("0704.0209", "cross", "cs.GT"),
            ListingItem("0704.0916", "cross", "cs.DL"),
        ]
        items4 = [
            ListingItem("0704.0091", "rep", "0704.0054"),
            ListingItem("0704.0225", "rep", "0704.0186"),
            ListingItem("0704.0847", "rep", "0704.0129"),
            ListingItem("0704.0257", "rep", "0704.0481"),
        ]

        lstgs: List[ListingItem] = items2 + items3 + items4
        return ListingNew(
            listings=lstgs[skip : skip + show],
            announced=datetime.date(2007, 4, 1),
            submitted=(datetime.date(2007, 3, 30), datetime.date(2007, 4, 1)),
            new_count=len(items2),
            cross_count=len(items3),
            rep_count=len(items4),
            expires="Wed, 21 Oct 2015 07:28:00 GMT",
        )

    def list_pastweek_articles(
        self,
        archiveOrCategory: str,
        skip: int,
        show: int,
        if_modified_since: Optional[str] = None,
    ) -> Listing:
        """Example of list_pastweek_articles."""
        listings = [
            "0704.0526",
            "0704.0988",
            "0704.0182",
            "0704.0310",
            "0704.0616",
            "0704.0732",
            "0704.0042",
            "0704.0615",
            "0704.0568",
            "0704.0319",
            "0704.0265",
            "0704.0133",
            "0704.0533",
            "0704.0453",
            "0704.0276",
            "0704.0991",
            "0704.0740",
            "0704.0473",
            "0704.0083",
            "0704.0278",
            "0704.0006",
            "0704.0735",
            "0704.0753",
            "0704.0324",
            "0704.0600",
            "0704.0737",
            "0704.0387",
            "0704.0659",
            "0704.0432",
            "0704.0408",
            "0704.0895",
            "0704.0088",
            "0704.0719",
            "0704.0124",
            "0704.0508",
        ]
        items2: List[ListingItem] = [
            ListingItem(id=id, listingType="new", primary="cs.DB") for id in listings
        ]

        # These dates are faked
        daysize = 7
        pd1 = (datetime.date(2007, 4, 2), 0)
        pd2 = (datetime.date(2007, 4, 3), daysize - 1)
        pd3 = (datetime.date(2007, 4, 4), daysize * 2 - 1)
        pd4 = (datetime.date(2007, 4, 5), daysize * 3 - 1)
        pd5 = (datetime.date(2007, 4, 6), daysize * 4 - 1)

        return Listing(
            listings=items2,
            pubdates=[pd1, pd2, pd3, pd4, pd5],
            count=len(listings),
            expires="Wed, 21 Oct 2015 07:28:00 GMT",
        )

    def list_articles_by_year(
        self,
        archiveOrCategory: str,
        year: int,
        skip: int,
        show: int,
        if_modified_since: Optional[str] = None,
    ) -> Listing:
        """Example of list_articles_by_year."""
        return self.list_articles_by_month(
            archiveOrCategory, year, 1, skip, show, if_modified_since
        )

    def list_articles_by_month(
        self,
        archiveOrCategory: str,
        year: int,
        month: int,
        skip: int,
        show: int,
        if_modified_since: Optional[str] = None,
    ) -> Listing:
        """Example of list_articles_by_month."""
        if "skip" not in vars():
            skip = 0
        if "show" not in vars():
            show = 25

        pd = datetime.date(2007, 4, 2)

        items2: List[ListingItem] = [
            ListingItem(id=id, listingType="new", primary="cs.DB")
            for id in k_listings[skip : skip + show]
        ]

        return Listing(
            listings=items2,
            pubdates=[(pd, len(k_listings))],
            count=len(k_listings),
            expires="Wed, 21 Oct 2015 07:28:00 GMT",
        )


k_listings = [
    "0704.0526",
    "0704.0988",
    "0704.0182",
    "0704.0310",
    "0704.0616",
    "0704.0732",
    "0704.0042",
    "0704.0615",
    "0704.0568",
    "0704.0319",
    "0704.0265",
    "0704.0133",
    "0704.0533",
    "0704.0453",
    "0704.0276",
    "0704.0991",
    "0704.0740",
    "0704.0473",
    "0704.0083",
    "0704.0278",
    "0704.0006",
    "0704.0735",
    "0704.0753",
    "0704.0324",
    "0704.0600",
    "0704.0737",
    "0704.0387",
    "0704.0659",
    "0704.0432",
    "0704.0408",
    "0704.0895",
    "0704.0088",
    "0704.0719",
    "0704.0124",
    "0704.0508",
    "0704.0145",
    "0704.0075",
    "0704.0333",
    "0704.0445",
    "0704.0226",
    "0704.0266",
    "0704.0368",
    "0704.0716",
    "0704.0373",
    "0704.0378",
    "0704.0536",
    "0704.0239",
    "0704.0209",
    "0704.0916",
    "0704.0091",
    "0704.0054",
    "0704.0225",
    "0704.0186",
    "0704.0847",
    "0704.0129",
    "0704.0257",
    "0704.0388",
    "0704.0481",
    "0704.0156",
    "0704.0685",
    "0704.0694",
    "0704.0485",
    "0704.0682",
    "0704.0200",
    "0704.0627",
    "0704.0722",
    "0704.0845",
    "0704.0815",
    "0704.0362",
    "0704.0143",
    "0704.0381",
    "0704.0299",
    "0704.0205",
    "0704.0914",
    "0704.0640",
    "0704.0683",
    "0704.0238",
    "0704.0939",
    "0704.0582",
    "0704.0019",
    "0704.0958",
    "0704.0150",
    "0704.0699",
    "0704.0306",
    "0704.0418",
    "0704.0463",
    "0704.0002",
    "0704.0975",
    "0704.0787",
    "0704.0597",
    "0704.0154",
    "0704.0178",
    "0704.0572",
    "0704.0576",
    "0704.0757",
    "0704.0457",
    "0704.0751",
    "0704.0414",
    "0704.0355",
    "0704.0349",
    "0704.0161",
    "0704.0748",
    "0704.0980",
    "0704.0016",
    "0704.0905",
    "0704.0596",
    "0704.0730",
    "0704.0543",
    "0704.0070",
    "0704.0898",
    "0704.0273",
    "0704.0480",
    "0704.0810",
    "0704.0440",
    "0704.0025",
    "0704.0361",
    "0704.0936",
    "0704.0770",
    "0704.0612",
    "0704.0255",
    "0704.0109",
    "0704.0625",
    "0704.0010",
    "0704.0015",
    "0704.0458",
    "0704.0856",
    "0704.0359",
    "0704.0406",
    "0704.0462",
    "0704.0614",
    "0704.0983",
    "0704.0142",
    "0704.0013",
    "0704.0578",
    "0704.0820",
    "0704.0477",
    "0704.0583",
    "0704.0111",
    "0704.0495",
    "0704.0282",
    "0704.0986",
    "0704.0586",
    "0704.0311",
    "0704.0700",
    "0704.0638",
    "0704.0206",
    "0704.0808",
    "0704.0389",
    "0704.0904",
    "0704.0105",
    "0704.0433",
    "0704.0434",
    "0704.0943",
    "0704.0422",
    "0704.0180",
    "0704.0199",
    "0704.0766",
    "0704.0077",
    "0704.0788",
    "0704.0170",
    "0704.0603",
    "0704.0844",
    "0704.0995",
    "0704.0948",
    "0704.0231",
    "0704.0103",
    "0704.0650",
    "0704.0944",
    "0704.0591",
    "0704.0404",
    "0704.0858",
    "0704.0956",
    "0704.0454",
    "0704.0676",
    "0704.0144",
    "0704.0190",
    "0704.0868",
    "0704.0363",
    "0704.0763",
    "0704.0026",
    "0704.0553",
    "0704.0104",
    "0704.0185",
    "0704.0575",
    "0704.0017",
    "0704.0702",
    "0704.0169",
    "0704.0632",
    "0704.0671",
    "0704.0177",
    "0704.0792",
    "0704.0849",
    "0704.0079",
    "0704.0559",
    "0704.0221",
    "0704.0896",
    "0704.0677",
    "0704.0938",
    "0704.0356",
    "0704.0035",
    "0704.0585",
    "0704.0254",
    "0704.0880",
    "0704.0537",
    "0704.0581",
    "0704.0646",
    "0704.0837",
    "0704.0681",
    "0704.0809",
    "0704.0761",
    "0704.0642",
    "0704.0566",
    "0704.0323",
    "0704.0891",
    "0704.0775",
    "0704.0240",
    "0704.0475",
    "0704.0262",
    "0704.0271",
    "0704.0023",
    "0704.0784",
    "0704.0528",
    "0704.0392",
    "0704.0869",
    "0704.0797",
    "0704.0673",
    "0704.0078",
    "0704.0790",
    "0704.0300",
    "0704.0569",
    "0704.0466",
    "0704.0555",
    "0704.0486",
    "0704.0365",
    "0704.0413",
    "0704.0181",
    "0704.0374",
    "0704.0018",
    "0704.0184",
    "0704.0758",
    "0704.0256",
    "0704.0386",
    "0704.0217",
    "0704.0224",
    "0704.0045",
    "0704.0573",
    "0704.0417",
    "0704.0663",
    "0704.0796",
    "0704.0253",
    "0704.0401",
    "0704.0126",
    "0704.0014",
    "0704.0229",
    "0704.0996",
    "0704.0046",
    "0704.0747",
    "0704.0656",
    "0704.0653",
    "0704.0274",
    "0704.0806",
    "0704.0216",
    "0704.0590",
    "0704.0309",
    "0704.0069",
    "0704.0873",
    "0704.0826",
    "0704.0135",
    "0704.0438",
    "0704.0421",
    "0704.0709",
    "0704.0455",
    "0704.0931",
    "0704.0328",
    "0704.0342",
    "0704.0967",
    "0704.0976",
    "0704.0604",
    "0704.0691",
    "0704.0020",
    "0704.0981",
    "0704.0482",
    "0704.0889",
    "0704.0029",
    "0704.0689",
    "0704.0041",
    "0704.0538",
    "0704.0860",
    "0704.0219",
    "0704.0963",
    "0704.0424",
    "0704.0918",
    "0704.0260",
    "0704.0613",
    "0704.0106",
    "0704.0467",
    "0704.0658",
    "0704.0701",
    "0704.0123",
    "0704.0259",
    "0704.0153",
    "0704.0379",
    "0704.0203",
    "0704.0158",
    "0704.0364",
    "0704.0520",
    "0704.0875",
    "0704.0913",
    "0704.0094",
    "0704.0004",
    "0704.0977",
    "0704.0964",
    "0704.0280",
    "0704.0383",
    "0704.0817",
    "0704.0426",
    "0704.0565",
    "0704.0439",
    "0704.0084",
    "0704.0675",
    "0704.0067",
    "0704.0704",
    "0704.0119",
    "0704.0781",
    "0704.0049",
    "0704.0628",
    "0704.0074",
    "0704.0377",
    "0704.0588",
    "0704.0196",
    "0704.0057",
    "0704.0416",
    "0704.0804",
    "0704.0828",
    "0704.0192",
    "0704.0649",
    "0704.0452",
    "0704.0402",
    "0704.0657",
    "0704.0073",
    "0704.0972",
    "0704.0919",
    "0704.0786",
    "0704.0420",
    "0704.0288",
    "0704.0080",
    "0704.0687",
    "0704.0448",
    "0704.0664",
    "0704.0742",
    "0704.0236",
    "0704.0647",
    "0704.0881",
    "0704.0354",
    "0704.0295",
    "0704.0780",
    "0704.0052",
    "0704.0794",
    "0704.0771",
    "0704.0497",
    "0704.0631",
    "0704.0863",
    "0704.0114",
    "0704.0030",
    "0704.0987",
    "0704.0312",
    "0704.0971",
    "0704.0344",
    "0704.0556",
    "0704.0012",
    "0704.0955",
    "0704.0782",
    "0704.0836",
    "0704.0261",
    "0704.0430",
    "0704.0304",
    "0704.0063",
    "0704.0696",
    "0704.0593",
    "0704.0965",
    "0704.0643",
    "0704.0241",
    "0704.0928",
    "0704.0864",
    "0704.0053",
    "0704.0773",
    "0704.0510",
    "0704.0879",
    "0704.0811",
    "0704.0038",
    "0704.0444",
    "0704.0194",
    "0704.0731",
    "0704.0277",
    "0704.0036",
    "0704.0511",
    "0704.0252",
    "0704.0922",
    "0704.0530",
    "0704.0945",
    "0704.0302",
    "0704.0580",
    "0704.0293",
    "0704.0227",
    "0704.0925",
    "0704.0842",
    "0704.0768",
    "0704.0545",
    "0704.0097",
    "0704.0008",
    "0704.0570",
    "0704.0450",
    "0704.0007",
    "0704.0684",
    "0704.0764",
    "0704.0370",
    "0704.0686",
    "0704.0552",
    "0704.0281",
    "0704.0279",
    "0704.0746",
    "0704.0071",
    "0704.0831",
    "0704.0358",
    "0704.0637",
    "0704.0179",
    "0704.0957",
    "0704.0244",
    "0704.0654",
    "0704.0841",
    "0704.0912",
    "0704.0315",
    "0704.0031",
    "0704.0729",
    "0704.0391",
    "0704.0660",
    "0704.0117",
    "0704.0403",
    "0704.0202",
    "0704.0644",
    "0704.0819",
    "0704.0855",
    "0704.0212",
    "0704.0474",
    "0704.0335",
    "0704.0110",
    "0704.0698",
    "0704.0610",
    "0704.0220",
    "0704.0139",
    "0704.0973",
    "0704.0491",
    "0704.0534",
    "0704.0215",
    "0704.0321",
    "0704.0409",
    "0704.0375",
    "0704.0267",
    "0704.0040",
    "0704.0648",
    "0704.0755",
    "0704.0507",
    "0704.0883",
    "0704.0316",
    "0704.0608",
    "0704.0172",
    "0704.0776",
    "0704.0814",
    "0704.0527",
    "0704.0242",
    "0704.0900",
    "0704.0039",
    "0704.0668",
    "0704.0589",
    "0704.0470",
    "0704.0283",
    "0704.0483",
    "0704.0560",
    "0704.0284",
    "0704.0669",
    "0704.0033",
    "0704.0056",
    "0704.0713",
    "0704.0307",
    "0704.0059",
    "0704.0412",
    "0704.0005",
    "0704.0937",
    "0704.0727",
    "0704.0690",
    "0704.0577",
    "0704.0926",
    "0704.0887",
    "0704.0750",
    "0704.0871",
    "0704.0332",
    "0704.0222",
    "0704.0385",
    "0704.0714",
    "0704.0992",
    "0704.0550",
    "0704.0602",
    "0704.0622",
    "0704.0756",
    "0704.0861",
    "0704.0923",
    "0704.0840",
    "0704.0917",
    "0704.0061",
    "0704.0308",
    "0704.0390",
    "0704.0852",
    "0704.0920",
    "0704.0011",
    "0704.0929",
    "0704.0739",
    "0704.0982",
    "0704.0606",
    "0704.0952",
    "0704.0759",
    "0704.0134",
    "0704.0651",
    "0704.0818",
    "0704.0609",
    "0704.0272",
    "0704.0120",
    "0704.0380",
    "0704.0197",
    "0704.0116",
    "0704.0962",
    "0704.0985",
    "0704.0515",
    "0704.0546",
    "0704.0141",
    "0704.0058",
    "0704.0850",
    "0704.0665",
    "0704.0187",
    "0704.0151",
    "0704.0661",
    "0704.0419",
    "0704.0851",
    "0704.0211",
    "0704.0953",
    "0704.0679",
    "0704.0720",
    "0704.0998",
    "0704.0168",
    "0704.0296",
    "0704.0807",
    "0704.0264",
    "0704.0670",
    "0704.0127",
    "0704.0825",
    "0704.0621",
    "0704.0791",
    "0704.0532",
    "0704.0496",
    "0704.0003",
    "0704.0247",
    "0704.0708",
    "0704.0492",
    "0704.0574",
    "0704.0927",
    "0704.0778",
    "0704.0951",
    "0704.0128",
    "0704.0372",
    "0704.0183",
    "0704.0949",
    "0704.0629",
    "0704.0915",
    "0704.0446",
    "0704.0544",
    "0704.0269",
    "0704.0132",
    "0704.0218",
    "0704.0443",
    "0704.0564",
    "0704.0662",
    "0704.0490",
    "0704.0326",
    "0704.0619",
    "0704.0394",
    "0704.0384",
    "0704.1001",
    "0704.0189",
    "0704.0032",
    "0704.0246",
    "0704.0540",
    "0704.0099",
    "0704.0942",
    "0704.0314",
    "0704.0369",
    "0704.0460",
    "0704.0655",
    "0704.0725",
    "0704.0353",
    "0704.0113",
    "0704.0890",
    "0704.0407",
    "0704.0340",
    "0704.0594",
    "0704.0521",
    "0704.0947",
    "0704.0346",
    "0704.0371",
    "0704.0557",
    "0704.0865",
    "0704.0138",
    "0704.0752",
    "0704.0697",
    "0704.0802",
    "0704.0095",
    "0704.0774",
    "0704.0037",
    "0704.0405",
    "0704.0493",
    "0704.0399",
    "0704.0347",
    "0704.0605",
    "0704.0548",
    "0704.0624",
    "0704.0089",
    "0704.0859",
    "0704.0712",
    "0704.0469",
    "0704.0044",
    "0704.0710",
    "0704.0395",
    "0704.0498",
    "0704.0155",
    "0704.0693",
    "0704.0870",
    "0704.0195",
    "0704.0535",
    "0704.0234",
    "0704.0513",
    "0704.0489",
    "0704.0055",
    "0704.0705",
    "0704.0472",
    "0704.0558",
    "0704.0567",
    "0704.0909",
    "0704.0680",
    "0704.0946",
    "0704.0478",
    "0704.0779",
    "0704.0598",
    "0704.0886",
    "0704.0519",
    "0704.0718",
    "0704.0494",
    "0704.0337",
    "0704.0345",
    "0704.0907",
    "0704.0098",
    "0704.0503",
    "0704.0523",
    "0704.0249",
    "0704.0518",
    "0704.0131",
    "0704.0331",
    "0704.0882",
    "0704.0862",
    "0704.0514",
    "0704.0248",
    "0704.0471",
    "0704.0799",
    "0704.0086",
    "0704.0911",
    "0704.0932",
    "0704.0082",
    "0704.0745",
    "0704.0641",
    "0704.0157",
    "0704.0022",
    "0704.0504",
    "0704.0198",
    "0704.0667",
    "0704.0562",
    "0704.0051",
    "0704.0213",
    "0704.0997",
    "0704.0695",
    "0704.0721",
    "0704.0028",
    "0704.0979",
    "0704.0666",
    "0704.0715",
    "0704.0984",
    "0704.0592",
    "0704.0313",
    "0704.0437",
    "0704.0093",
    "0704.0579",
    "0704.0343",
    "0704.0298",
    "0704.0250",
    "0704.0848",
    "0704.0336",
    "0704.0885",
    "0704.0674",
    "0704.0672",
    "0704.0783",
    "0704.0549",
    "0704.0633",
    "0704.0148",
    "0704.0969",
    "0704.0382",
    "0704.0339",
    "0704.0839",
    "0704.0176",
    "0704.0894",
    "0704.0853",
    "0704.0048",
    "0704.0744",
    "0704.0954",
    "0704.0149",
    "0704.0101",
    "0704.0163",
    "0704.0587",
    "0704.0941",
    "0704.0906",
    "0704.0723",
    "0704.0191",
    "0704.0411",
    "0704.0174",
    "0704.0130",
    "0704.0329",
    "0704.0884",
    "0704.0152",
    "0704.0902",
    "0704.0769",
    "0704.0160",
    "0704.0034",
    "0704.0484",
    "0704.0289",
    "0704.0122",
    "0704.0193",
    "0704.0888",
    "0704.0171",
    "0704.0072",
    "0704.0789",
    "0704.0733",
    "0704.0096",
    "0704.0398",
    "0704.0827",
    "0704.0275",
    "0704.0367",
    "0704.0500",
    "0704.0501",
    "0704.0066",
    "0704.0159",
    "0704.0531",
    "0704.0341",
    "0704.0994",
    "0704.0136",
    "0704.0711",
    "0704.0024",
    "0704.0214",
    "0704.0966",
    "0704.0021",
    "0704.0634",
    "0704.0924",
    "0704.0062",
    "0704.0232",
    "0704.0813",
    "0704.0400",
    "0704.0270",
    "0704.0125",
    "0704.0547",
    "0704.0188",
    "0704.0060",
    "0704.0449",
    "0704.0167",
    "0704.0734",
    "0704.0173",
    "0704.0352",
    "0704.0459",
    "0704.0903",
    "0704.0854",
    "0704.0652",
    "0704.0601",
    "0704.0736",
    "0704.0561",
    "0704.0237",
    "0704.0468",
    "0704.0974",
    "0704.0506",
    "0704.0857",
    "0704.1000",
    "0704.0618",
    "0704.0833",
    "0704.0290",
    "0704.0112",
    "0704.0935",
    "0704.0910",
    "0704.0465",
    "0704.0940",
    "0704.0607",
    "0704.0243",
    "0704.0425",
    "0704.0047",
    "0704.0517",
    "0704.0617",
    "0704.0305",
    "0704.0824",
    "0704.0741",
    "0704.0393",
    "0704.0798",
    "0704.0085",
    "0704.0423",
    "0704.0456",
    "0704.0717",
    "0704.0263",
    "0704.0286",
    "0704.0505",
    "0704.0001",
    "0704.0800",
    "0704.0726",
    "0704.0950",
    "0704.0027",
    "0704.0738",
    "0704.0464",
    "0704.0303",
    "0704.0442",
    "0704.0933",
    "0704.0436",
    "0704.0121",
    "0704.0108",
    "0704.0294",
    "0704.0223",
    "0704.0164",
    "0704.0846",
    "0704.0777",
    "0704.0301",
    "0704.0350",
    "0704.0563",
    "0704.0930",
    "0704.0892",
    "0704.0692",
    "0704.0921",
    "0704.0816",
    "0704.0959",
    "0704.0623",
    "0704.0050",
    "0704.0812",
    "0704.0678",
    "0704.0645",
    "0704.0318",
    "0704.0843",
    "0704.0410",
    "0704.0571",
    "0704.0076",
    "0704.0897",
    "0704.0635",
    "0704.0043",
    "0704.0429",
    "0704.0706",
    "0704.0901",
    "0704.0512",
    "0704.0765",
    "0704.0877",
    "0704.0584",
    "0704.0251",
    "0704.0829",
    "0704.0990",
    "0704.0626",
    "0704.0525",
    "0704.0934",
    "0704.0830",
    "0704.0081",
    "0704.0874",
    "0704.0823",
    "0704.0838",
    "0704.0524",
    "0704.0551",
    "0704.0834",
    "0704.0065",
    "0704.0805",
    "0704.0728",
    "0704.0993",
    "0704.0207",
    "0704.0754",
    "0704.0760",
    "0704.0487",
    "0704.0291",
    "0704.0140",
    "0704.0989",
    "0704.0832",
    "0704.0447",
    "0704.0327",
    "0704.0961",
    "0704.0529",
    "0704.0878",
    "0704.0599",
    "0704.0115",
    "0704.0516",
    "0704.0201",
    "0704.0322",
    "0704.0165",
    "0704.0688",
    "0704.0068",
    "0704.0268",
    "0704.0821",
    "0704.0908",
    "0704.0724",
    "0704.0999",
    "0704.0228",
    "0704.0090",
    "0704.0107",
    "0704.0866",
    "0704.0803",
    "0704.0100",
    "0704.0461",
    "0704.0509",
    "0704.0795",
    "0704.0801",
    "0704.0366",
    "0704.0317",
    "0704.0541",
    "0704.0630",
    "0704.0539",
    "0704.0338",
    "0704.0175",
    "0704.0703",
    "0704.0488",
    "0704.0210",
    "0704.0707",
    "0704.0431",
    "0704.0639",
    "0704.0785",
    "0704.0441",
    "0704.0204",
    "0704.0330",
    "0704.0357",
    "0704.0334",
    "0704.0292",
    "0704.0064",
    "0704.0960",
    "0704.0762",
    "0704.0245",
    "0704.0872",
    "0704.0970",
    "0704.0087",
    "0704.0867",
    "0704.0893",
    "0704.0620",
    "0704.0092",
    "0704.0351",
    "0704.0502",
    "0704.0235",
    "0704.0978",
    "0704.0749",
    "0704.0396",
    "0704.0348",
    "0704.0772",
    "0704.0137",
    "0704.0822",
    "0704.0258",
    "0704.0435",
    "0704.0233",
    "0704.0611",
    "0704.0499",
    "0704.0451",
    "0704.0360",
    "0704.0636",
    "0704.0285",
    "0704.0554",
    "0704.0899",
    "0704.0147",
    "0704.0427",
    "0704.0208",
    "0704.0476",
    "0704.0479",
    "0704.0230",
    "0704.0166",
    "0704.0118",
    "0704.0595",
    "0704.0009",
    "0704.0743",
    "0704.0102",
    "0704.0835",
    "0704.0320",
    "0704.0162",
    "0704.0428",
    "0704.0146",
    "0704.0876",
    "0704.0325",
    "0704.0542",
    "0704.0376",
    "0704.0297",
    "0704.0397",
    "0704.0968",
    "0704.0415",
    "0704.0793",
    "0704.0287",
    "0704.0767",
    "0704.0522",
]
