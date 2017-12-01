---
UID: NF.prcomoem.IPrintOemUI.GetInfo
title: IPrintOemUI::GetInfo
author: windows-driver-content
description: A user interface plug-in's IPrintOemUI::GetInfo method returns identification information.
old-location: print\iprintoemui_getinfo.htm
old-project: print
ms.assetid: be1eb547-f824-4d6d-818f-8ac1740d1d24
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUI, GetInfo, IPrintOemUI::GetInfo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemUI.GetInfo
req.alt-loc: Prcomoem.h
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
req.iface: IPrintOemUI
req.product: Windows 10 or later.
---

# IPrintOemUI::GetInfo method



## -description
<p>A user interface plug-in's <code>IPrintOemUI::GetInfo</code> method returns identification information.</p>


## -syntax

````
STDMETHOD GetInfo(
   DWORD  dwMode,
   PVOID  pBuffer,
   DWORD  cbSize,
   PDWORD pcbNeeded
);
````


## -parameters
<dl>

### -param <i>dwMode</i> 

<dd>
<p>Contains one of the following caller-supplied integer constants.</p>
<p></p>
<dl>

### -param <a id="OEMGI_GETREQUESTEDHELPERINTERFACES"></a><a id="oemgi_getrequestedhelperinterfaces"></a>OEMGI_GETREQUESTEDHELPERINTERFACES

<dd>
<p>The method must write the bit flag value of OEMPUBLISH_IPRINTCOREHELPER to the buffer <i>pBuffer</i> if the <a href="print.iprintoemui_publishdriverinterface">IPrintOemUI::PublishDriverInterface</a> method should be called with parameter <i>pIUnknown</i> pointing to an object that implements the <a href="print.iprintcorehelperps_interface">IPrintCoreHelperPS Interface</a> or <a href="print.iprintcorehelperuni_interface">IPrintCoreHelperUni Interface</a>.</p>
</dd>
</dl>
<p></p>
<dl>

### -param <a id="OEMGI_GETSIGNATURE"></a><a id="oemgi_getsignature"></a>OEMGI_GETSIGNATURE

<dd>
<p>The method must return a unique four-byte identification signature. The plug-in must also place this signature in <a href="..\compstui\ns-compstui--optitem.md">OPTITEM</a> structures, as described in the description of the <a href="..\printoem\ns-printoem--oemcuipparam.md">OEMCUIPPARAM</a> structure's <b>pOEMOptItems</b> member.</p>
</dd>
</dl>
<p></p>
<dl>

### -param <a id="OEMGI_GETVERSION"></a><a id="oemgi_getversion"></a>OEMGI_GETVERSION

<dd>
<p>The method must return the user interface plug-in's version number as a DWORD. The version format is developer-defined.</p>
</dd>
</dl>
</dd>

### -param <i>pBuffer</i> 

<dd>
<p>Caller-supplied pointer to memory allocated to receive the information specified by <i>dwMode</i>.</p>
</dd>

### -param <i>cbSize</i> 

<dd>
<p>Caller-supplied size of the buffer pointed to by <i>pBuffer</i>.</p>
</dd>

### -param <i>pcbNeeded</i> 

<dd>
<p>Caller-supplied pointer to a location to receive the number of bytes written into the buffer pointed to by <i>pBuffer</i>.</p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

## -remarks
<p>User interface plug-ins are required to implement the <code>IPrintOemUI::GetInfo</code> method, which is called immediately after the plug-in is loaded. The method should return the specified information by writing it to the address specified by <i>pBuffer</i> and writing the size, in bytes, of the returned information into the location specified by <i>pcbNeeded</i>.</p>

<p>If <i>pBuffer</i> is <b>NULL</b>, the method should just use <i>pcbNeeded</i> to return the number of bytes required to store the specified information.</p>

<p>For more information about creating and installing user interface plug-ins, see <a href="NULL">Customizing Microsoft's Printer Drivers</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Prcomoem.h (include Prcomoem.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="print.iprintoemps_getinfo">IPrintOemPS::GetInfo</a>
</dt>
<dt>
<a href="print.iprintoemuni_getinfo">IPrintOemUni::GetInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUI::GetInfo method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
