---
UID: NS.winsplp._PRINTPROCESSOROPENDATA
title: PRINTPROCESSOROPENDATA
author: windows-driver-content
description: The PRINTPROCESSOROPENDATA structure is used as an input parameter to a print processor's OpenPrintProcessor function.
old-location: print\printprocessoropendata.htm
old-project: print
ms.assetid: d7160747-d81c-407a-bbf0-7ec5b3210c13
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: PRINTPROCESSOROPENDATA, PRINTPROCESSOROPENDATA, *PPRINTPROCESSOROPENDATA, *LPPRINTPROCESSOROPENDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: winsplp.h
req.include-header: Winsplp.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PRINTPROCESSOROPENDATA
req.alt-loc: winsplp.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# PRINTPROCESSOROPENDATA structure



## -description
<p>The PRINTPROCESSOROPENDATA structure is used as an input parameter to a print processor's <a href="..\winsplp\nf-winsplp-openprintprocessor.md">OpenPrintProcessor</a> function.</p>


## -syntax

````
typedef struct _PRINTPROCESSOROPENDATA {
  PDEVMODE pDevMode;
  LPWSTR   pDatatype;
  LPWSTR   pParameters;
  LPWSTR   pDocumentName;
  DWORD    JobId;
  LPWSTR   pOutputFile;
  LPWSTR   pPrinterName;
} PRINTPROCESSOROPENDATA, *PPRINTPROCESSOROPENDATA, *LPPRINTPROCESSOROPENDATA;
````


## -struct-fields
<dl>

### -field <b>pDevMode</b>

<dd>
<p>Spooler-supplied pointer to a <a href="display.devmodew">DEVMODEW</a> structure.</p>
</dd>

### -field <b>pDatatype</b>

<dd>
<p>Spooler-supplied pointer to a string representing the print job's data type.</p>
</dd>

### -field <b>pParameters</b>

<dd>
<p>Spooler-supplied pointer to a parameter string, as specified in a JOB_INFO_2 structure supplied to a call to the <b>SetJob</b> function, described in the Microsoft Windows SDK documentation.</p>
</dd>

### -field <b>pDocumentName</b>

<dd>
<p>Spooler-supplied pointer to a string representing the name of the input document associated with the print job. </p>
</dd>

### -field <b>JobId</b>

<dd>
<p>Spooler-supplied value identifying the print job.</p>
</dd>

### -field <b>pOutputFile</b>

<dd>
<p>Spooler-supplied pointer to a string representing the name of the output spool file.</p>
</dd>

### -field <b>pPrinterName</b>

<dd>
<p>Spooler-supplied pointer to a string representing the name of the printer to be used.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winsplp.h (include Winsplp.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\winsplp\nf-winsplp-openprintprocessor.md">OpenPrintProcessor</a>
</dt>
<dt>
<a href="display.devmodew">DEVMODEW</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20PRINTPROCESSOROPENDATA structure%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
