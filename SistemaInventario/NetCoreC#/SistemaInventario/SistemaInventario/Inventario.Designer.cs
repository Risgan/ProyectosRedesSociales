namespace SistemaInventario
{
    partial class Inventario
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            groupBox3 = new GroupBox();
            btn_kardex = new Button();
            btn_salida = new Button();
            btn_entrada = new Button();
            groupBox2 = new GroupBox();
            inp_cantidad = new NumericUpDown();
            inp_producto = new TextBox();
            inp_fecha = new DateTimePicker();
            inp_documento = new NumericUpDown();
            inp_cu = new MaskedTextBox();
            lbl_fecha = new Label();
            lbl_producto = new Label();
            lbl_cantidad = new Label();
            lbl_documento = new Label();
            lbl_cu = new Label();
            groupBox1 = new GroupBox();
            dataGridView = new DataGridView();
            fecha = new DataGridViewTextBoxColumn();
            producto = new DataGridViewTextBoxColumn();
            descripcion = new DataGridViewTextBoxColumn();
            documento = new DataGridViewTextBoxColumn();
            entrada = new DataGridViewTextBoxColumn();
            salida = new DataGridViewTextBoxColumn();
            saldo = new DataGridViewTextBoxColumn();
            costoUnitario = new DataGridViewTextBoxColumn();
            total = new DataGridViewTextBoxColumn();
            panel1.SuspendLayout();
            groupBox3.SuspendLayout();
            groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)inp_cantidad).BeginInit();
            ((System.ComponentModel.ISupportInitialize)inp_documento).BeginInit();
            groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)dataGridView).BeginInit();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.Controls.Add(groupBox3);
            panel1.Controls.Add(groupBox2);
            panel1.Controls.Add(groupBox1);
            panel1.Dock = DockStyle.Fill;
            panel1.Location = new Point(0, 0);
            panel1.Name = "panel1";
            panel1.Size = new Size(1106, 680);
            panel1.TabIndex = 0;
            // 
            // groupBox3
            // 
            groupBox3.Controls.Add(btn_kardex);
            groupBox3.Controls.Add(btn_salida);
            groupBox3.Controls.Add(btn_entrada);
            groupBox3.Font = new Font("Arial", 15.75F);
            groupBox3.Location = new Point(487, 12);
            groupBox3.Name = "groupBox3";
            groupBox3.Size = new Size(144, 251);
            groupBox3.TabIndex = 10;
            groupBox3.TabStop = false;
            groupBox3.Text = "Acciones";
            // 
            // btn_kardex
            // 
            btn_kardex.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            btn_kardex.Font = new Font("Arial", 15.75F);
            btn_kardex.Location = new Point(18, 127);
            btn_kardex.Name = "btn_kardex";
            btn_kardex.Size = new Size(108, 39);
            btn_kardex.TabIndex = 3;
            btn_kardex.Text = "Kardex";
            btn_kardex.UseVisualStyleBackColor = true;
            btn_kardex.Click += btn_kardex_Click;
            // 
            // btn_salida
            // 
            btn_salida.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            btn_salida.Font = new Font("Arial", 15.75F);
            btn_salida.Location = new Point(18, 82);
            btn_salida.Name = "btn_salida";
            btn_salida.Size = new Size(108, 39);
            btn_salida.TabIndex = 2;
            btn_salida.Text = "Salida";
            btn_salida.UseVisualStyleBackColor = true;
            btn_salida.Click += btn_salida_Click;
            // 
            // btn_entrada
            // 
            btn_entrada.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            btn_entrada.Font = new Font("Arial", 15.75F);
            btn_entrada.Location = new Point(18, 37);
            btn_entrada.Name = "btn_entrada";
            btn_entrada.Size = new Size(108, 39);
            btn_entrada.TabIndex = 1;
            btn_entrada.Text = "Entrada";
            btn_entrada.UseVisualStyleBackColor = true;
            btn_entrada.Click += btn_entrada_Click;
            // 
            // groupBox2
            // 
            groupBox2.Controls.Add(inp_cantidad);
            groupBox2.Controls.Add(inp_producto);
            groupBox2.Controls.Add(inp_fecha);
            groupBox2.Controls.Add(inp_documento);
            groupBox2.Controls.Add(inp_cu);
            groupBox2.Controls.Add(lbl_fecha);
            groupBox2.Controls.Add(lbl_producto);
            groupBox2.Controls.Add(lbl_cantidad);
            groupBox2.Controls.Add(lbl_documento);
            groupBox2.Controls.Add(lbl_cu);
            groupBox2.Font = new Font("Arial", 15.75F);
            groupBox2.Location = new Point(15, 12);
            groupBox2.Name = "groupBox2";
            groupBox2.Size = new Size(466, 251);
            groupBox2.TabIndex = 9;
            groupBox2.TabStop = false;
            groupBox2.Text = "Campos";
            // 
            // inp_cantidad
            // 
            inp_cantidad.Location = new Point(211, 115);
            inp_cantidad.Name = "inp_cantidad";
            inp_cantidad.Size = new Size(232, 32);
            inp_cantidad.TabIndex = 16;
            // 
            // inp_producto
            // 
            inp_producto.Location = new Point(211, 74);
            inp_producto.Name = "inp_producto";
            inp_producto.Size = new Size(232, 32);
            inp_producto.TabIndex = 15;
            // 
            // inp_fecha
            // 
            inp_fecha.Location = new Point(211, 33);
            inp_fecha.Name = "inp_fecha";
            inp_fecha.Size = new Size(232, 32);
            inp_fecha.TabIndex = 14;
            // 
            // inp_documento
            // 
            inp_documento.Location = new Point(211, 197);
            inp_documento.Maximum = new decimal(new int[] { 99999999, 0, 0, 0 });
            inp_documento.Name = "inp_documento";
            inp_documento.Size = new Size(232, 32);
            inp_documento.TabIndex = 13;
            // 
            // inp_cu
            // 
            inp_cu.Location = new Point(211, 156);
            inp_cu.Name = "inp_cu";
            inp_cu.Size = new Size(232, 32);
            inp_cu.TabIndex = 11;
            // 
            // lbl_fecha
            // 
            lbl_fecha.AutoSize = true;
            lbl_fecha.Font = new Font("Arial", 15.75F);
            lbl_fecha.Location = new Point(112, 37);
            lbl_fecha.Name = "lbl_fecha";
            lbl_fecha.Size = new Size(75, 24);
            lbl_fecha.TabIndex = 2;
            lbl_fecha.Text = "Fecha:";
            // 
            // lbl_producto
            // 
            lbl_producto.AutoSize = true;
            lbl_producto.Font = new Font("Arial", 15.75F);
            lbl_producto.Location = new Point(87, 78);
            lbl_producto.Name = "lbl_producto";
            lbl_producto.Size = new Size(100, 24);
            lbl_producto.TabIndex = 4;
            lbl_producto.Text = "Producto:";
            // 
            // lbl_cantidad
            // 
            lbl_cantidad.AutoSize = true;
            lbl_cantidad.Font = new Font("Arial", 15.75F);
            lbl_cantidad.Location = new Point(88, 119);
            lbl_cantidad.Name = "lbl_cantidad";
            lbl_cantidad.Size = new Size(99, 24);
            lbl_cantidad.TabIndex = 5;
            lbl_cantidad.Text = "Cantidad:";
            // 
            // lbl_documento
            // 
            lbl_documento.AutoSize = true;
            lbl_documento.Font = new Font("Arial", 15.75F);
            lbl_documento.Location = new Point(65, 201);
            lbl_documento.Name = "lbl_documento";
            lbl_documento.Size = new Size(122, 24);
            lbl_documento.TabIndex = 7;
            lbl_documento.Text = "Documento:";
            // 
            // lbl_cu
            // 
            lbl_cu.AutoSize = true;
            lbl_cu.Font = new Font("Arial", 15.75F);
            lbl_cu.Location = new Point(37, 160);
            lbl_cu.Name = "lbl_cu";
            lbl_cu.Size = new Size(150, 24);
            lbl_cu.TabIndex = 6;
            lbl_cu.Text = "Costo Unitario:";
            // 
            // groupBox1
            // 
            groupBox1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            groupBox1.Controls.Add(dataGridView);
            groupBox1.Font = new Font("Arial", 15.75F);
            groupBox1.Location = new Point(12, 269);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(1082, 399);
            groupBox1.TabIndex = 0;
            groupBox1.TabStop = false;
            groupBox1.Text = "Grilla";
            // 
            // dataGridView
            // 
            dataGridView.AllowUserToAddRows = false;
            dataGridView.AllowUserToDeleteRows = false;
            dataGridView.AllowUserToOrderColumns = true;
            dataGridView.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridView.Columns.AddRange(new DataGridViewColumn[] { fecha, producto, descripcion, documento, entrada, salida, saldo, costoUnitario, total });
            dataGridView.Dock = DockStyle.Fill;
            dataGridView.Location = new Point(3, 28);
            dataGridView.Name = "dataGridView";
            dataGridView.ReadOnly = true;
            dataGridView.Size = new Size(1076, 368);
            dataGridView.TabIndex = 0;
            // 
            // fecha
            // 
            fecha.HeaderText = "Fecha";
            fecha.Name = "fecha";
            fecha.ReadOnly = true;
            // 
            // producto
            // 
            producto.HeaderText = "Producto";
            producto.Name = "producto";
            producto.ReadOnly = true;
            // 
            // descripcion
            // 
            descripcion.HeaderText = "Descripción";
            descripcion.Name = "descripcion";
            descripcion.ReadOnly = true;
            // 
            // documento
            // 
            documento.HeaderText = "Documento";
            documento.Name = "documento";
            documento.ReadOnly = true;
            // 
            // entrada
            // 
            entrada.HeaderText = "Entrada";
            entrada.Name = "entrada";
            entrada.ReadOnly = true;
            // 
            // salida
            // 
            salida.HeaderText = "Salida";
            salida.Name = "salida";
            salida.ReadOnly = true;
            // 
            // saldo
            // 
            saldo.HeaderText = "Saldo";
            saldo.Name = "saldo";
            saldo.ReadOnly = true;
            // 
            // costoUnitario
            // 
            costoUnitario.HeaderText = "Costo Unitario";
            costoUnitario.Name = "costoUnitario";
            costoUnitario.ReadOnly = true;
            // 
            // total
            // 
            total.HeaderText = "Total";
            total.Name = "total";
            total.ReadOnly = true;
            // 
            // Inventario
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1106, 680);
            Controls.Add(panel1);
            Name = "Inventario";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "Inventario";
            WindowState = FormWindowState.Maximized;
            panel1.ResumeLayout(false);
            groupBox3.ResumeLayout(false);
            groupBox2.ResumeLayout(false);
            groupBox2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)inp_cantidad).EndInit();
            ((System.ComponentModel.ISupportInitialize)inp_documento).EndInit();
            groupBox1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)dataGridView).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private GroupBox groupBox1;
        private Button btn_entrada;
        private TextBox inp_producto;
        private Label lbl_fecha;
        private DataGridView dataGridView;
        private Label lbl_documento;
        private Label lbl_cu;
        private Label lbl_cantidad;
        private Label lbl_producto;
        private DateTimePicker inp_fecha;
        private GroupBox groupBox3;
        private GroupBox groupBox2;
        private NumericUpDown numericUpDown1;
        private TextBox textBox2;
        private MaskedTextBox inp_cu;
        private NumericUpDown inp_documento;
        private Button btn_kardex;
        private Button btn_salida;
        private NumericUpDown inp_cantidad;
        private DataGridViewTextBoxColumn fecha;
        private DataGridViewTextBoxColumn producto;
        private DataGridViewTextBoxColumn descripcion;
        private DataGridViewTextBoxColumn documento;
        private DataGridViewTextBoxColumn entrada;
        private DataGridViewTextBoxColumn salida;
        private DataGridViewTextBoxColumn saldo;
        private DataGridViewTextBoxColumn costoUnitario;
        private DataGridViewTextBoxColumn total;
    }
}