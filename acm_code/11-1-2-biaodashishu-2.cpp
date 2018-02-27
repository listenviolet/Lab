#include <iostream>
#include <cstring>
#include <stack>
using namespace std;

struct Node
{
    char data;
    Node *left, *right;
    Node(char c) : data(c), left(NULL),right(NULL){}
};

Node *create_ET(char *src)
{
    cout << "*src: " << *src << endl;
    stack<Node*> st;
    char *s = src;
    Node *temp;
    while(*s)
    {
        if(*s == '+' || *s == '-' || *s == '*' || *s =='/')
        {
            temp = new Node(*s);
            temp -> right = st.top();
            char rtop = st.top() -> data;
            cout << "right top: " << rtop << endl;
            st.pop();
            temp -> left = st.top();
            char ltop = st.top() -> data;
            cout << "left top: " << ltop << endl;
            st.pop();
            st.push(temp);
            cout << "push: " << temp -> data << endl;
        }
        else
        {
            temp = new Node(*s);
            cout << "push: " << temp -> data << endl;
            st.push(temp);
        }
        s++;
    }

    return st.top();
}

void postOrder(Node *root)
{
    if(root != NULL)
    {
        postOrder(root -> left);
        postOrder(root -> right);
        cout << root -> data << ' ';
    }
}

int prior(char op)
{
    if(op == '+' || op == '-') return 1;
    else if(op == '*' || op == '/') return 2;
    return 0;
}

string middleToLast(string middata)
{
    stack<char> op;
    string ans;
    for(int i = 0; i < middata.size(); ++i)
    {
        char c = middata[i];
        if(c >= 'a' && c <= 'z') ans.append(1, c);
        else if(c == '(') op.push('(');
        else if(c == ')')
        {
            while(op.top()!='(')
            {
                ans.append(1, op.top());
                op.pop();
            }
            op.pop();
        }
        else if(op.empty()) op.push(c);
        else if(prior(c) > prior(op.top())) op.push(c);
        else if(prior(c) <= prior(op.top()))
        {
            while(!op.empty() && prior(c) <= prior(op.top()))
            {
                ans.append(1, op.top());
                op.pop();
            }
            op.push(c);
        }
    }
    while(!op.empty())
    {
        ans.append(1, op.top());
        op.pop();
    }

    return ans;
}

int main()
{
    string middata, lastdata;
    cin >> middata;
    lastdata = middleToLast(middata);
    for(int i = 0; i < lastdata.size(); ++i)
    {
        if(i == 0)
            cout << lastdata[i];
        else cout << ' ' << lastdata[i];
    }
    cout << endl;
    cout << "-------------------" << endl;

    cout << "lastdata.size(): " << lastdata.size() << endl;
    char ldata[lastdata.size()];
    for(int i = 0; i < lastdata.size(); ++i)
    {
        ldata[i] = lastdata[i];
    }

    char *p = ldata;
    while(*p)
    {
        cout << *p++;
    }
    cout <<endl;
    Node *r = create_ET(ldata);
    postOrder(r);
    return 0;
}
//a+b*(c-d)-e/f
