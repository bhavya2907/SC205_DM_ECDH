class point:
    def __init__(self,x1,y1):
        self.x=x1
        self.y=y1

def inverse(x):
    for i in range (p):
        if (x*i)%p==1:
            return i

def ispoint(c):
    yp=(c.y*c.y)%p
    xp=(c.x*c.x*c.x+a*c.x+b)%p
    if xp==yp:
        return True
    else:
        return False

def allpoints(p,a,b):
    for i in range (0,p):
        for j in range (0,p):
            c=point(i,j)
            if ispoint(c)==True:
                print("(",i,",",j,")")
                
def addpoints(c1,c2):
    if c1.x==c2.x and c1.y!=c2.y:
        print("Point at infinity")
    if c1.x==c2.x and c1.y==c2.y:
        s=((3*c1.x*c1.x+a)*inverse(2*c1.y))%p
        x1=(s*s-c1.x-c2.x)%p
        y1=(s*(c1.x-x1)-c1.y)%p
        c3=point(x1,y1)
        return c3
    else:
        s=((c2.y-c1.y)*inverse(c2.x-c1.x))%p
        x1=(s*s-c1.x-c2.x)%p
        y1=(s*(c1.x-x1)-c1.y)%p
        c3=point(x1,y1)
        return c3

def mult(n,g1):
    g2=g1
    i=1
    while i<n: 
        if g1.x==g2.x and g1.y!=g2.y:
            if i==n-1:
               print("point at infinity,  ",end="") 
               g2.x=0
               g2.y=0
               return g2
               i=i+1
               
            if i==n-2:
                return g1
            else:
                g2=g1
                i=i+2
                    
        if g1.x==g2.x and g1.y==g2.y:
            s=((3*g1.x*g1.x+a)*inverse(2*g1.y))%p
            x1=(s*s-g1.x-g2.x)%p
            y1=(s*(g1.x-x1)-g1.y)%p
            g2=point(x1,y1)
            i+=1
        else:
            s=((g2.y-g1.y)*inverse(g2.x-g1.x))%p
            x1=(s*s-g1.x-g2.x)%p
            y1=(s*(g1.x-x1)-g1.y)%p
            g2=point(x1,y1)

            i+=1
    return g2


f=1
choice=int(input("1.Details about elliptic curve\n2.Diffie Hellman implementation\n3.Exit\n"))
if choice==3:
        print("Thank you for using our code")
        quit()
a=int(input("Enter curve parameter a: "))
b=int(input("Enter curve parameter b: "))
p=int(input("Enter curve parameter p: "))

while(choice==1 or choice==2):

    if choice==1:
               
        while f==1:
            print("What would you like to do?")
            print("1.See all points on curve \n2.Add two points \n3.Multiply a point\n4.Change the curve\n5.Exit")
            ch=int(input(""))
            if ch==1:
                allpoints(p,a,b)
            if ch==2:
                x1=int(input("x1:"))
                y1=int(input("y1:"))
                x2=int(input("x2:"))
                y2=int(input("y2:"))
                c1=point(x1,y1)
                c2=point(x2,y2)
                c3=addpoints(c1,c2)
                print("(",c3.x,",",c3.y,")")
            if ch==3:
                x1=int(input("x1:"))
                y1=int(input("y1:"))
                k=int(input("k:"))
                c1=point(x1,y1)
                c4=mult(k,c1)
                print("(",c4.x,",",c4.y,")")
            if ch==4:
                a=int(input("a:"))
                b=int(input("b:"))
                p=int(input("p:"))
            if ch==5:
                break
            print("To continue,press 1, else press 0")
            f=int(input(""))

    if choice==2:
        alpha=int(input("Enter private key for Alice ranging from 1 to p: "))
        beta=int(input("Enter private key for Bob ranging from 1 to p: "))
        genx=int(input("Enter x coordinate of generator point: "))
        geny=int(input("Enter y coordinate of generator point: "))
        genp=point(genx,geny)
        a_pub=mult(alpha,genp)
        b_pub=mult(beta,genp)
        print("Alice's public key is: ")
        print("(",a_pub.x,",",a_pub.y,")")
        print("Bob's public key is: ")
        print("(",b_pub.x,",",b_pub.y,")")
        print("Bob and Alice will exchange these public keys and multiply them with their private keys")
        a_sec=mult(alpha,b_pub)
        b_sec=mult(beta,a_pub)
        print("Alice's private key is: ")
        print("(",a_sec.x,",",a_sec.y,")")
        print("Bob's private key is: ")
        print("(",b_sec.x,",",b_sec.y,")")
        print("We can see that these are same, and thus they can use this to encrypt a message or create another ket from this")
        choice=int(input("1.Details about elliptic curve\n2.Diffie Hellman implementation\n3.Exit\n"))

    
        
        

    else:
        choice=int(input("1.Details about elliptic curve\n2.Diffie Hellman implementation\n3.Exit\n"))
