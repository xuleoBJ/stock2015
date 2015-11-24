namespace mainStock
{
    partial class mainForm
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
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tbgStart = new System.Windows.Forms.TabPage();
            this.tbgPatternRec = new System.Windows.Forms.TabPage();
            this.tbgRiskManage = new System.Windows.Forms.TabPage();
            this.tbgMoneyManage = new System.Windows.Forms.TabPage();
            this.tbgTradeCal = new System.Windows.Forms.TabPage();
            this.tbgWebInforFetch = new System.Windows.Forms.TabPage();
            this.menuStripTop = new System.Windows.Forms.MenuStrip();
            this.系统ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.帮助ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.label1 = new System.Windows.Forms.Label();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.tbgStockSelect = new System.Windows.Forms.TabPage();
            this.tabControl1.SuspendLayout();
            this.tbgStart.SuspendLayout();
            this.menuStripTop.SuspendLayout();
            this.SuspendLayout();
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tbgStart);
            this.tabControl1.Controls.Add(this.tbgPatternRec);
            this.tabControl1.Controls.Add(this.tbgRiskManage);
            this.tabControl1.Controls.Add(this.tbgMoneyManage);
            this.tabControl1.Controls.Add(this.tbgTradeCal);
            this.tabControl1.Controls.Add(this.tbgWebInforFetch);
            this.tabControl1.Controls.Add(this.tbgStockSelect);
            this.tabControl1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tabControl1.Location = new System.Drawing.Point(0, 25);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(683, 438);
            this.tabControl1.TabIndex = 0;
            // 
            // tbgStart
            // 
            this.tbgStart.Controls.Add(this.textBox2);
            this.tbgStart.Controls.Add(this.label2);
            this.tbgStart.Controls.Add(this.textBox1);
            this.tbgStart.Controls.Add(this.label1);
            this.tbgStart.Location = new System.Drawing.Point(4, 22);
            this.tbgStart.Name = "tbgStart";
            this.tbgStart.Padding = new System.Windows.Forms.Padding(3);
            this.tbgStart.Size = new System.Drawing.Size(675, 412);
            this.tbgStart.TabIndex = 0;
            this.tbgStart.Text = "每日提醒";
            this.tbgStart.UseVisualStyleBackColor = true;
            // 
            // tbgPatternRec
            // 
            this.tbgPatternRec.Location = new System.Drawing.Point(4, 22);
            this.tbgPatternRec.Name = "tbgPatternRec";
            this.tbgPatternRec.Padding = new System.Windows.Forms.Padding(3);
            this.tbgPatternRec.Size = new System.Drawing.Size(675, 412);
            this.tbgPatternRec.TabIndex = 1;
            this.tbgPatternRec.Text = "模式识别";
            this.tbgPatternRec.UseVisualStyleBackColor = true;
            // 
            // tbgRiskManage
            // 
            this.tbgRiskManage.Location = new System.Drawing.Point(4, 22);
            this.tbgRiskManage.Name = "tbgRiskManage";
            this.tbgRiskManage.Size = new System.Drawing.Size(675, 412);
            this.tbgRiskManage.TabIndex = 2;
            this.tbgRiskManage.Text = "风险控制";
            this.tbgRiskManage.UseVisualStyleBackColor = true;
            // 
            // tbgMoneyManage
            // 
            this.tbgMoneyManage.Location = new System.Drawing.Point(4, 22);
            this.tbgMoneyManage.Name = "tbgMoneyManage";
            this.tbgMoneyManage.Size = new System.Drawing.Size(675, 412);
            this.tbgMoneyManage.TabIndex = 3;
            this.tbgMoneyManage.Text = "仓位管理";
            this.tbgMoneyManage.UseVisualStyleBackColor = true;
            // 
            // tbgTradeCal
            // 
            this.tbgTradeCal.Location = new System.Drawing.Point(4, 22);
            this.tbgTradeCal.Name = "tbgTradeCal";
            this.tbgTradeCal.Size = new System.Drawing.Size(675, 412);
            this.tbgTradeCal.TabIndex = 4;
            this.tbgTradeCal.Text = "量化交易";
            this.tbgTradeCal.UseVisualStyleBackColor = true;
            // 
            // tbgWebInforFetch
            // 
            this.tbgWebInforFetch.Location = new System.Drawing.Point(4, 22);
            this.tbgWebInforFetch.Name = "tbgWebInforFetch";
            this.tbgWebInforFetch.Size = new System.Drawing.Size(675, 412);
            this.tbgWebInforFetch.TabIndex = 5;
            this.tbgWebInforFetch.Text = "信息获取";
            this.tbgWebInforFetch.UseVisualStyleBackColor = true;
            // 
            // menuStripTop
            // 
            this.menuStripTop.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.系统ToolStripMenuItem,
            this.帮助ToolStripMenuItem});
            this.menuStripTop.Location = new System.Drawing.Point(0, 0);
            this.menuStripTop.Name = "menuStripTop";
            this.menuStripTop.Size = new System.Drawing.Size(683, 25);
            this.menuStripTop.TabIndex = 1;
            this.menuStripTop.Text = "menuStrip1";
            // 
            // 系统ToolStripMenuItem
            // 
            this.系统ToolStripMenuItem.Name = "系统ToolStripMenuItem";
            this.系统ToolStripMenuItem.Size = new System.Drawing.Size(44, 21);
            this.系统ToolStripMenuItem.Text = "系统";
            // 
            // 帮助ToolStripMenuItem
            // 
            this.帮助ToolStripMenuItem.Name = "帮助ToolStripMenuItem";
            this.帮助ToolStripMenuItem.Size = new System.Drawing.Size(44, 21);
            this.帮助ToolStripMenuItem.Text = "帮助";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(21, 45);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(53, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "上证市值";
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(80, 42);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(100, 21);
            this.textBox1.TabIndex = 1;
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(80, 74);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(100, 21);
            this.textBox2.TabIndex = 3;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(21, 77);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(53, 12);
            this.label2.TabIndex = 2;
            this.label2.Text = "深圳市值";
            // 
            // tbgStockSelect
            // 
            this.tbgStockSelect.Location = new System.Drawing.Point(4, 22);
            this.tbgStockSelect.Name = "tbgStockSelect";
            this.tbgStockSelect.Padding = new System.Windows.Forms.Padding(3);
            this.tbgStockSelect.Size = new System.Drawing.Size(675, 412);
            this.tbgStockSelect.TabIndex = 6;
            this.tbgStockSelect.Text = "选票系统";
            this.tbgStockSelect.UseVisualStyleBackColor = true;
            // 
            // mainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(683, 463);
            this.Controls.Add(this.tabControl1);
            this.Controls.Add(this.menuStripTop);
            this.MainMenuStrip = this.menuStripTop;
            this.Name = "mainForm";
            this.Text = "基于模式识别的Stock交易系统";
            this.tabControl1.ResumeLayout(false);
            this.tbgStart.ResumeLayout(false);
            this.tbgStart.PerformLayout();
            this.menuStripTop.ResumeLayout(false);
            this.menuStripTop.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tbgStart;
        private System.Windows.Forms.TabPage tbgPatternRec;
        private System.Windows.Forms.TabPage tbgRiskManage;
        private System.Windows.Forms.TabPage tbgMoneyManage;
        private System.Windows.Forms.TabPage tbgTradeCal;
        private System.Windows.Forms.TabPage tbgWebInforFetch;
        private System.Windows.Forms.MenuStrip menuStripTop;
        private System.Windows.Forms.ToolStripMenuItem 系统ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 帮助ToolStripMenuItem;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TabPage tbgStockSelect;
    }
}

