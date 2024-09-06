using System; 
using System.Collections.Generic; 
using System.ComponentModel; 
using System.Data; 
using System.Drawing; 
using System.Linq; 
using System.Text; 
using System.Windows.Forms; 
using System.Data.SqlClient; 
 
namespace Finger_ATM 
{ 
    public partial class AdminLogin: Form 
    { 
        SqlConnection con = new SqlConnection(@"Data Source=DESKTOP
68SHPBA\SQLEXPRESS;Initial Catalog=FingerVote;Integrated Security=True");  
        public AdminLogin() 
        { 
            InitializeComponent(); 
        } 
 
        private void groupBox1_Enter(object sender, EventArgs e) 
        { 
 
        } 
 
        private void button1_Click(object sender, EventArgs e) 
        { 
            SqlCommand cmd = new SqlCommand("Select Pass from Admin where Id = 
'"+textBox1.Text+"'",con); 
            con.Open(); 
            SqlDataReader dr = cmd.ExecuteReader(); 
            if (dr.HasRows) 
            { 
                dr.Read(); 
                if (dr[0].ToString() == textBox2.Text)
                 { 
                    con.Close(); 
                    this.Hide(); 
                    AdminMenu am = new AdminMenu(); 
                    am.Show(); 
                } 
                else 
                { 
                    con.Close(); 
                    MessageBox.Show("Invalid Password", "Error !!!", 
MessageBoxButtons.OK, MessageBoxIcon.Error); 
                } 
            } 
            else 
            { 
                MessageBox.Show("Invalid ID","Error 
!!!",MessageBoxButtons.OK,MessageBoxIcon.Error); 
            } 
        } 
 
        private void AdminLogin_Load(object sender, EventArgs e) 
        { 
             
        } 
 
        private void button2_Click(object sender, EventArgs e) 
        { 
            TakeElection te = new TakeElection(); 
            te.Show(); 
            this.Hide(); 
        } 
    } 
} 
