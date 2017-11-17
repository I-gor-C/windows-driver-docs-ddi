---
UID: NF.prcomoem.IPrintOemPS.GetInfo
title: IPrintOemPS::GetInfo
author: windows-driver-content
description: A rendering plug-in's IPrintOemPS::GetInfo method returns identification information.
old-location: print\iprintoemps_getinfo.htm
ms.assetid: 9a8b060d-675b-4171-b75e-6df55cd0667f
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
req.alt-api: IPrintOemPS.GetInfo
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
ms.keywords: IPrintOemPS, GetInfo, IPrintOemPS::GetInfo
req.iface: IPrintOemPS
req.product: Windows 10 or later.
---

# IPrintOemPS::GetInfo method



## -description
<p>A rendering plug-in's <code>IPrintOemPS::GetInfo</code> method returns identification information.</p>


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

### -param <a id="OEMGI_GETPUBLISHERINFO"></a><a id="oemgi_getpublisherinfo"></a>OEMGI_GETPUBLISHERINFO

<dd>
<p>The method must indicate whether the rendering plug-in will be using "publishing mode". The <i>pBuffer</i> parameter points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561851">PUBLISHERINFO</a> structure, to be filled in by the method. For more information, see the following Remarks section.</p>
</dd>
</dl>
<p></p>
<dl>

### -param <a id="OEMGI_GETREQUESTEDHELPERINTERFACES"></a><a id="oemgi_getrequestedhelperinterfaces"></a>OEMGI_GETREQUESTEDHELPERINTERFACES

<dd>
<p>The method must write the bit flag value of OEMPUBLISH_IPRINTCOREHELPER to the buffer <i>pBuffer</i> if the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553228">IPrintOemPS::PublishDriverInterface</a> method should be called with parameter <i>pIUnknown</i> pointing to an object that implements the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552906">IPrintCoreHelperPS Interface</a>.</p>
</dd>
</dl>
<p></p>
<dl>

### -param <a id="OEMGI_GETSIGNATURE"></a><a id="oemgi_getsignature"></a>OEMGI_GETSIGNATURE

<dd>
<p>The method must return a unique four-byte identification signature. The plug-in must also place this signature in <a href="https://msdn.microsoft.com/library/windows/hardware/ff559656">OPTITEM</a> structures, as described in the description of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557653">OEMCUIPPARAM</a>. structure's <b>pOEMOptItems</b> member.</p>
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
</dl><p>The operation failed</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

## -remarks
<p>Rendering plug-ins for Pscript5 are required to implement the <code>IPrintOemPS::GetInfo</code> method, which is called immediately after the plug-in is loaded. The method should return the specified information by writing it to the address specified by <i>pBuffer</i> and writing the size, in bytes, of the returned information into the location specified by <i>pcbNeeded</i>.</p>

<p>If <i>pBuffer</i> is <b>NULL</b>, the method should just use <i>pcbNeeded</i> to return the number of bytes required to store the specified information.</p>

<p>In "publishing mode", all font information to be downloaded is placed in the job header. Each font is downloaded only once and can be used for any page, allowing the job to be page-order independent. If <i>dwMode</i> is OEMGI_GETPUBLISHERINFO but the plug-in does not support publishing mode, <code>IPrintOemPS::GetInfo</code> should return E_NOTIMPL.</p>

<p>For more information about creating and installing rendering plug-ins, see <a href="NULL">Customizing Microsoft's Printer Drivers</a>.</p>

<p>Rendering plug-ins for Pscript5 are required to implement the <code>IPrintOemPS::GetInfo</code> method, which is called immediately after the plug-in is loaded. The method should return the specified information by writing it to the address specified by <i>pBuffer</i> and writing the size, in bytes, of the returned information into the location specified by <i>pcbNeeded</i>.</p>

<p>If <i>pBuffer</i> is <b>NULL</b>, the method should just use <i>pcbNeeded</i> to return the number of bytes required to store the specified information.</p>

<p>In "publishing mode", all font information to be downloaded is placed in the job header. Each font is downloaded only once and can be used for any page, allowing the job to be page-order independent. If <i>dwMode</i> is OEMGI_GETPUBLISHERINFO but the plug-in does not support publishing mode, <code>IPrintOemPS::GetInfo</code> should return E_NOTIMPL.</p>

<p>For more information about creating and installing rendering plug-ins, see <a href="NULL">Customizing Microsoft's Printer Drivers</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554178">IPrintOemUI::GetInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554256">IPrintOemUni::GetInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemPS::GetInfo method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
