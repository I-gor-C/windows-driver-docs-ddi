---
UID: NS.printoem._OEMCUIPPARAM~r1
title: OEMCUIPPARAM
author: windows-driver-content
description: The OEMCUIPPARAM structure is used as an input parameter to a user interface plug-in's IPrintOemUI::CommonUIProp method.
old-location: print\oemcuipparam.htm
old-project: print
ms.assetid: 178b635c-0916-44f5-87a3-a2766601dcab
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: OEMCUIPPARAM, OEMCUIPPARAM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: printoem.h
req.include-header: Printoem.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OEMCUIPPARAM
req.alt-loc: printoem.h
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
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# OEMCUIPPARAM structure



## -description
<p>The OEMCUIPPARAM structure is used as an input parameter to a user interface plug-in's <a href="print.iprintoemui_commonuiprop">IPrintOemUI::CommonUIProp</a> method.</p>


## -syntax

````
typedef struct _OEMCUIPPARAM {
  DWORD           cbSize;
  POEMUIOBJ       poemuiobj;
  HANDLE          hPrinter;
  PWSTR           pPrinterName;
  HANDLE          hModule;
  HANDLE          hOEMHeap;
  PDEVMODE        pPublicDM;
  PVOID           pOEMDM;
  DWORD           dwFlags;
  POPTITEM        pDrvOptItems;
  DWORD           cDrvOptItems;
  POPTITEM        pOEMOptItems;
  DWORD           cOEMOptItems;
  PVOID           pOEMUserData;
  OEMCUIPCALLBACK OEMCUIPCallback;
} OEMCUIPPARAM;
````


## -struct-fields
<dl>

### -field cbSize

<dd>
<p>Size of the OEMCUIPPARAM structure. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field poemuiobj

<dd>
<p>Pointer to an <a href="..\printoem\ns-printoem--oemuiobj.md">OEMUIOBJ</a> structure.</p>
</dd>

### -field hPrinter

<dd>
<p>Handle to the printer. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field pPrinterName

<dd>
<p>String containing the printer name. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field hModule

<dd>
<p>Handle to the user interface plug-in. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field hOEMHeap

<dd>
<p>Handle to a heap from which space can be allocated by calling the <b>HeapAlloc</b> function (described in the Microsoft Windows SDK documentation). Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field pPublicDM

<dd>
<p>Pointer to the printer's public DEVMODEW structure. Valid only if the <a href="print.iprintoemui_commonuiprop">IPrintOemUI::CommonUIProp</a> method's <i>dwMode</i> argument is OEMCUIP_DOCPROP. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field pOEMDM

<dd>
<p>Pointer to the user interface plug-in's private DEVMODEW members. Valid only if the <b>IPrintOemUI::CommonUIProp</b> method's <i>dwMode</i> argument is OEMCUIP_DOCPROP. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field dwFlags

<dd>
<p></p>
<dl>

### -field For calls to IPrintOemUI::CommonUIProp with its dwMode parameter set to OEMCUIP_DOCPROP:

<dd>
<p>Contains the contents of the <b>fMode</b> member of the <a href="..\winddiui\ns-winddiui--documentpropertyheader.md">DOCUMENTPROPERTYHEADER</a> structure received by the printer driver's <a href="..\winddiui\nf-winddiui-drvdocumentpropertysheets.md">DrvDocumentPropertySheets</a> function.</p>
</dd>

### -field For calls to IPrintOemUI::CommonUIProp with its dwMode parameter set to OEMCUIP_PRNPROP:

<dd>
<p>Contains the contents of the <b>Flags</b> member of the DEVICEPROPERTYHEADER structure received by the printer driver's <a href="..\winddiui\nf-winddiui-drvdevicepropertysheets.md">DrvDevicePropertySheets</a> function.</p>
</dd>
</dl>
</dd>

### -field pDrvOptItems

<dd>
<p>Pointer to the printer driver's <a href="..\compstui\ns-compstui--optitem.md">OPTITEM</a> array. Not valid the first time <b>IPrintOemUI::CommonUIProp</b> is called. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field cDrvOptItems

<dd>
<p>Count of OPTITEM structures in the array pointed to by <b>pDrvOptItems</b>. Supplied by the Unidrv or Pscript5 driver.</p>
</dd>

### -field pOEMOptItems

<dd>
<p>Pointer to an array of OPTITEM structures. Supplied by <b>IPrintOemUI::CommonUIProp</b> caller. The second time the <b>IPrintOemUI::CommonUIProp</b> method is called, it must place OPTITEM structures defined by the user interface plug-in in this array, and it must place the structure count in <b>cOEMOptItems</b>. For each OPTITEM structure placed in the array, you must do the following:</p>
<ul>
<li>
<p>Set the OPTITEM structure's <b>DMPubID</b> member either to one of the predefined values or to a value greater than DMPUB_USER. If you use any predefined values, you must search through the entire OPTITEM array for structures already containing those values, and you must set their OPTIF_HIDE flags.</p>
</li>
<li>
<p>Allocate space for OPTTYPES and OPTPARAMS structures by calling the Windows SDK <b>HeapAlloc</b> function, using the handle contained in the OEMCUIPPARAM structure's <b>hOEMHeap</b> member. The printer driver deallocates this space when it is no longer needed.</p>
</li>
</ul>
<p>Not valid the first time <b>IPrintOemUI::CommonUIProp</b> is called.</p>
</dd>

### -field cOEMOptItems

<dd>
<p>Count of OPTITEM structures contained in the array pointed by <b>pOEMOptItems</b>. Supplied by the Unidrv or Pscript5 driver.</p>
<p>The first time the <b>IPrintOemUI::CommonUIProp</b> method is called, the caller-supplied value for <b>cOEMOptItems</b> is zero. The <b>IPrintOemUI::CommonUIProp</b> method must change this value to indicate the number of OPTITEM structures that the method supplies. The second time it is called, <b>IPrintOemUI::CommonUIProp</b> must supply the number of OPTITEM structures actually added to the array pointed to by <b>pOEMOptItems</b>.</p>
</dd>

### -field pOEMUserData

<dd>
<p>Used by the <b>IPrintOemUI::CommonUIProp</b> method, the second time it is called, to provide the <b>OEMCUIPCallback</b> function with optional extra input information.</p>
</dd>

### -field OEMCUIPCallback

<dd>
<p>Used by the <b>IPrintOemUI::CommonUIProp</b> method, the second time it is called, to return the address of a callback function of type <a href="..\printoem\nc-printoem-oemcuipcallback.md">OEMCUIPCALLBACK</a>.</p>
</dd>
</dl>

## -remarks
<p>A user interface plug-in receives this structure's address as an input argument to both its <a href="print.iprintoemui_commonuiprop">IPrintOemUI::CommonUIProp</a> method and its <a href="..\printoem\nc-printoem-oemcuipcallback.md">OEMCUIPCALLBACK</a>-typed callback function.</p>

<p>For additional information about the use of this structure and associated functions, see <a href="https://msdn.microsoft.com/22ac2af6-37d8-4913-95af-9c3dc8576d40">User Interface Plug-Ins</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Printoem.h (include Printoem.h)</dt>
</dl>
</td>
</tr>
</table>