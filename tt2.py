"""
I.OOP
*object oriented programing:Lap trinh huong doi tuong
-dua cac su vat su viec hay cac chu the ben ngoai doi song vao trong moi truong code
-Khac han voi nhung gi tu trc gio em hay hoc 
+vi du nhu mik viet 1 cai function no se di theo trinh tu tu tren xuong duoi tu nhung cai da co suy ra nhung cai chua co va tinh toan
+oop thi mik se phai tu design 1 cai doi tuong nao do ma cta muon tim hieu,bao gom cai thon tin, dac diem cua doi tuong do va ca nhung thao tac hanh dong cua doi tuong do
*co 2 tu khoa quan trong trong oop 
-class:
+Nhu mot ban mau hay mot khuon mau tao ra cac doi tuong co cung dac tinh tuong tu nhau
-object:
+La cac doi tuong de trien khai cai ban thiet ke do
.attribuets:la cac thong tin de mieu ta doi tuong
.methods:la cac thao tac hay cac hanh dong cua doi tuong do
-cau truc cua 1 class:
class tenlop:
    attributes
    methods
-VD:
class car:
    hangsx
    loaixe
    mausac
    namsx

    def chay()
    def phanh()
    def dung()
-de ma tao cac object tu 1 class thi cai method dau tien phai tao do chinh la method init, o cac ngon ngu khac hay con goi constructor
-1 so kieu phuong thuc
+classmethod:dc phep truy cap vao lop lay va thay doi du lieu cua lop
+staticmethod:ko dc phep truy cap hay ko dc phep biet trang thai cua lop do la gi chi thao tac tren cac tham so dc truyen vao
II.Tinh chat quan trong cua oop
1.Tinh ke thua
-dua tren nhung class cu de viet ra cac class moi
-chung se ke thua nhung thuoc tinh, phuong thuc cua cac class cu do
-co the them cac thuoc tinh moi cho cac class moi do
2.Tinh dong goi
-bao ve cac thong tin ben trong han che quyen truy cap hay chinh sua du lieu tu ben ngoai
-3 pham vi truy cap
+public:Bat ki cac lop nao cx co the truy cap dc hoac goi phuong thuc 
+protected:Chi co lop hien tai va lop con moi dc truy cap hoaj goi phuong thuc
+private:chi trong lop hien tai moi dc truy cap
.muon truy cap vao va thay doi phai su dung getter va setter
getter:dung de lay gia tri
setter:dung de thay doi gia tri
3.Tinh da hinh
-1 phuong thuc nhung dat vao 2 class khac nhau thi se tra ve ket qua khac nhau
4.Tinh truu tuong
-truu tuong hoa cac doi tuong
-neu ra cai tong quat, ko neu ra cai cu the chi tiet
VD:khi di pha cafe ta chi viec bam may cai nut pha cafe thoi con viec lam ra cafe ntn thi mik ko qtam
-Để định nghĩa một lớp trừu tượng trong Python, bạn cần kế thừa từ ABC (Abstract Base Class) và sử dụng decorator @abstractmethod để đánh dấu các phương thức trừu tượng.
"""
class Car():
    #bien cua lop
    gia=50
    #Ham khoi tao
    def __init__(self,hangsx,mausac,namsx,giaxe):
        self.mausac=mausac
        self.namsx=namsx
        self._giaxe=giaxe#protected
        self.__hangsx=hangsx#private
        #getter lay gia tri ra
    def get_hangsx(self):
        return  self.__hangsx
        #setter thay doi gia tri
    def set_hangsx(self,x):
        self.__hangsx=x
    def chay(self):
        print("Chay nhanh")
    def dung(self):
        print("dung hoi lau")
    @classmethod
    def gia(cls):
        cls.gia=100
        return cls.gia
    @staticmethod
    def thue(thuexe):
        thuexe=thuexe*0.1
        return thuexe
class Tesla(Car):
    def __init__(self, hangsx, mausac, namsx, giaxe,loaixe):
      self.loaixe=loaixe
      super().__init__(hangsx, mausac, namsx, giaxe)
        #super() no dai dien cho lop cha dc cac lop con ke thua lai<
    def tuoi(self):
        return 10
class Vinfast(Car):
    def __init__(self, hangsx, mausac, namsx, giaxe,loaixe):
      self.loaixe=loaixe
      super().__init__(hangsx, mausac, namsx, giaxe)
    def tuoi(self):
        return 20
class Toyota(Vinfast):
    def __init__(self, hangsx, mausac, namsx, giaxe, loaixe):
        super().__init__(hangsx, mausac, namsx, giaxe, loaixe)
vinfast=Vinfast("vinfast","trang",2024,10000,"oto")
tesla=Tesla("tesla","dien",2018,1000,"dien")
honda=Car("honda","den",2018,1000)
toyota=Toyota("toyota","hong",2010,1500,"dien")
#classmethods
# Car.gia()
# print(Car.gia)
#staticmethod
# print(honda.thue(1000))
#dong goi 
# honda.set_hangsx("honda")
# print(honda.get_hangsx())
# print(toyota._giaxe)
#da hinh
print(vinfast.tuoi())
print(tesla.tuoi())