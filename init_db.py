from app import app
from models import db, Product

def init_db():
    with app.app_context():
        # 確保所有資料表存在
        db.create_all()

        # 檢查是否已經有商品資料
        if Product.query.first() is None:
            # 新增測試商品
            products = [
                Product(
                    name='測試商品1',
                    price=100,
                    description='這是測試商品1的描述',
                    stock=10,
                    category='測試類別'
                ),
                Product(
                    name='測試商品2',
                    price=200,
                    description='這是測試商品2的描述',
                    stock=20,
                    category='測試類別'
                ),
                Product(
                    name='測試商品3',
                    price=300,
                    description='這是測試商品3的描述',
                    stock=30,
                    category='測試類別'
                )
            ]

            # 新增到資料庫
            for product in products:
                db.session.add(product)
            
            # 提交變更
            db.session.commit()
            print('測試資料已新增完成！')
        else:
            print('資料庫中已有商品資料！')

if __name__ == '__main__':
    init_db()