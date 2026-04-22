<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
    <xsl:template match="/">
        <html>
            <head>
                <title>Student Records</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f5f5f5;
                        padding: 20px;
                    }
                    h1 {
                        text-align: center;
                        color: #333;
                        margin-bottom: 30px;
                    }
                    table {
                        width: 100%;
                        max-width: 900px;
                        margin: 0 auto;
                        border-collapse: collapse;
                        background-color: white;
                        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
                    }
                    th {
                        background-color: #4CAF50;
                        color: white;
                        padding: 15px;
                        text-align: left;
                        font-weight: bold;
                        border: 1px solid #45a049;
                    }
                    td {
                        padding: 12px 15px;
                        border: 1px solid #ddd;
                        text-align: left;
                    }
                    tr:nth-child(even) {
                        background-color: #f9f9f9;
                    }
                    tr:hover {
                        background-color: #f0f0f0;
                    }
                    tr:first-child {
                        background-color: #4CAF50;
                        color: white;
                    }
                    .container {
                        max-width: 900px;
                        margin: 0 auto;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Student Records</h1>
                    <table>
                        <thead>
                            <tr>
                                <th>Student ID</th>
                                <th>Name</th>
                                <th>Branch</th>
                                <th>Marks</th>
                            </tr>
                        </thead>
                        <tbody>
                            <xsl:for-each select="students/student">
                                <tr>
                                    <td><xsl:value-of select="id"/></td>
                                    <td><xsl:value-of select="name"/></td>
                                    <td><xsl:value-of select="branch"/></td>
                                    <td><xsl:value-of select="marks"/></td>
                                </tr>
                            </xsl:for-each>
                        </tbody>
                    </table>
                </div>
            </body>
        </html>
    </xsl:template>
    
</xsl:stylesheet>
