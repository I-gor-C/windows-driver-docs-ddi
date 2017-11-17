---
UID: NF.prcomoem.IPrintOemUni.TTYGetInfo
title: IPrintOemUni::TTYGetInfo
author: windows-driver-content
description: The IPrintOemUni::TTYGetInfo method enables a rendering plug-in to supply Unidrv with information relevant to text-only printers.
old-location: print\iprintoemuni_ttygetinfo.htm
ms.assetid: 0df8c555-4298-47e7-a6a7-43f101620e04
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemUni.TTYGetInfo
req.alt-loc: prcomoem.h
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
ms.keywords: IPrintOemUni, TTYGetInfo, IPrintOemUni::TTYGetInfo
req.iface: IPrintOemUni
req.product: Windows 10 or later.
---

# IPrintOemUni::TTYGetInfo method



## -description
<p>The <code>IPrintOemUni::TTYGetInfo</code> method enables a rendering plug-in to supply Unidrv with information relevant to text-only printers.</p>


## -syntax

````
HRESULT TTYGetInfo(
   PDEVOBJ pdevobj,
   DWORD   dwInfoIndex,
   PVOID   pOutputBuf,
   DWORD   dwSize,
   DWORD   *pcbcNeeded
);
````


## -parameters
<dl>

### -param <i>pdevobj</i> 

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547573">DEVOBJ</a> structure.</p>
</dd>

### -param <i>dwInfoIndex</i> 

<dd>
<p>Caller-supplied constant identifying the type of information being requested. The following constant values are defined:</p>
<p></p>
<dl>

### -param <a id="OEMTTY_INFO_CODEPAGE"></a><a id="oemtty_info_codepage"></a>OEMTTY_INFO_CODEPAGE

<dd>
<p>The <i>pOutputBuf</i> parameter points to a DWORD in which the method should return the number of the code page to be used.</p>
</dd>
</dl>
<p></p>
<dl>

### -param <a id="OEMTTY_INFO_MARGINS"></a><a id="oemtty_info_margins"></a>OEMTTY_INFO_MARGINS

<dd>
<p>The <i>pOutputBuf</i> parameter points to a RECT structure in which the method should return page margin widths, in tenths of millimeters (for example, 20 represents 2 mm). If the entire page is printable, all margin values must be 0.</p>
</dd>
</dl>
<p></p>
<dl>

### -param <a id="OEMTTY_INFO_NUM_UFMS_"></a><a id="oemtty_info_num_ufms_"></a>OEMTTY_INFO_NUM_UFMS 

<dd>
<p>The <i>pOutputBuf</i> parameter points to a DWORD in which the method should return the number of resource IDs of the <a href="wdkgloss.u#wdkgloss.unidrv_font_metrics__ufm_#wdkgloss.unidrv_font_metrics__ufm_"><i>UFMs</i></a> for 10, 12, and 17 CPI fonts. To actually obtain these resource IDs, perform a query using OEMTTY_INFO_UFM_IDS.</p>
</dd>
</dl>
<p></p>
<dl>

### -param <a id="OEMTTY_INFO_UFM_IDS_"></a><a id="oemtty_info_ufm_ids_"></a>OEMTTY_INFO_UFM_IDS 

<dd>
<p>The <i>pOutputBuf</i> parameter points to an array of DWORDs of sufficient size to hold the number of resource IDs of the UFMs for 10, 12, and 17 CPI fonts. (This number is obtained by using OEMTTY_INFO_NUM_UFMS in a query.) The method should return the resource IDs of the <a href="wdkgloss.u#wdkgloss.unidrv_font_metrics__ufm_#wdkgloss.unidrv_font_metrics__ufm_"><i>UFMs</i></a> for 10,12, and 17 CPI fonts. </p>
</dd>
</dl>
</dd>

### -param <i>pOutputBuf</i> 

<dd>
<p>Caller-supplied pointer to a buffer to receive the requested information.</p>
</dd>

### -param <i>dwSize</i> 

<dd>
<p>Caller-supplied size, in bytes, of the buffer pointed to by <i>pOutputBuf</i>.</p>
</dd>

### -param <i>pcbcNeeded</i> 

<dd>
<p>Caller-supplied pointer to a location to receive the number of bytes written into the buffer pointed to by <i>pOutputBuf</i>. If the number of bytes required is smaller than the number specified by <i>dwSize</i>, the method should supply the required size and return E_FAIL.</p>
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
<p>The <code>IPrintOemUni::TTYGetInfo</code> method is optional. If a rendering plug-in implements this method, the plug-in's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554253">IPrintOemUni::GetImplementedMethod</a> method must return S_OK when it receives "TTYGetInfo" as input.</p>

<p>The <code>IPrintOemUni::TTYGetInfo</code> method is optional. If a rendering plug-in implements this method, the plug-in's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554253">IPrintOemUni::GetImplementedMethod</a> method must return S_OK when it receives "TTYGetInfo" as input.</p>

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