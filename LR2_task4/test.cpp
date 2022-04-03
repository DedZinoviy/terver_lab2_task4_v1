#include <cfixcc.h>

class ModuleTest : public cfixcc::TextFixture
{
    public: 
        testAbs()
        {
            CFIX_ASSERT_MESSAGE(abs(1) == 1, "Метод не сработал на тесте с положительным числом");
            CFIX_ASSERT_MESSAGE(abs(-1) == 1, "Метод не сработал на тесте с отрицательным числом");
            CFIX_ASSERT_MESSAGE(abs(0) == 0, "Метод не сработал на тесте с нулём");

        }
}


CFIXCC_BIGIN_CLASS(ModuleTest);
CFIXCC_METOD()

int* prepare_memory(){
int* array= (int*)malloc(1024);
if(array == NULL)
    throw "insoficient memory"; 
memset(array, 0, 1024);
return array;
}

try{
int* arr = prepare_memory();
}catch(std::bad_alloc &except /*const char * message*/)
{
    printf("%s", message);
}




#include <QTest.h>

