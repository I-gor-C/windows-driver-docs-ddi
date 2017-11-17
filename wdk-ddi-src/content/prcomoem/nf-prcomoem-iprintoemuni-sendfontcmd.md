---
UID: NF.prcomoem.IPrintOemUni.SendFontCmd
title: IPrintOemUni::SendFontCmd
author: windows-driver-content
description: The IPrintOemUni::SendFontCmd method enables a rendering plug-in to modify a printer's font selection command and then send it to the printer.
old-location: print\iprintoemuni_sendfontcmd.htm
ms.assetid: b90a94d1-c6f3-483c-b5fc-edfee27094ab
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
req.alt-api: IPrintOemUni.SendFontCmd
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
ms.keywords: IPrintOemUni, SendFontCmd, IPrintOemUni::SendFontCmd
req.iface: IPrintOemUni
req.product: Windows 10 or later.
---

# IPrintOemUni::SendFontCmd method



## -description
<p>The <code>IPrintOemUni::SendFontCmd</code> method enables a rendering plug-in to modify a printer's font selection command and then send it to the printer.</p>


## -syntax

````
HRESULT SendFontCmd(
   PDEVOBJ      pdevobj,
   PUNIFONTOBJ  pUFObj,
   PFINVOCATION pFInv
);
````


## -parameters
<dl>

### -param <i>pdevobj</i> 

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547573">DEVOBJ</a> structure.</p>
</dd>

### -param <i>pUFObj</i> 

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563590">UNIFONTOBJ</a> structure.</p>
</dd>

### -param <i>pFInv</i> 

<dd>
<p>Caller-supplied pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548846">FINVOCATION</a> structure.</p>
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
<p>The <code>IPrintOemUni::SendFontCmd</code> method is used for selecting device fonts on printers that do not recognize the <a href="wdkgloss.p#wdkgloss.pcl#wdkgloss.pcl"><i>PCL</i></a>, CAPSL, or PPDS-formatted font commands supported by Unidrv. Its purpose is to allow a rendering plug-in to modify the font selection command that is specified in the font's .ufm (Unidrv Font Metrics) file. (To see how the command is stored, refer to the description of .ufm file's <a href="https://msdn.microsoft.com/library/windows/hardware/ff562872">UNIDRVINFO</a> structure.) If the command needs to be modified before being sent to the printer, you should implement the <code>IPrintOemUni::SendFontCmd</code> method.</p>

<p>The method receives the command string in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548846">FINVOCATION</a> structure pointed to by <i>pFInv</i>. Typically, the string contains variables for which values must be supplied. For example, the following font selection command requires that <i>#FontHeight</i> and <i>#FontWidth</i> be replaced with numeric values:</p>

<p>Current values for the font height and width can be obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff563594">UNIFONTOBJ_GetInfo</a> to read Unidrv's standard variables.</p>

<p>Whenever the <code>IPrintOemUni::SendFontCmd</code> method called, it must send the command string to the printer by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff553138">IPrintOemDriverUni::DrvWriteSpoolBuf</a>.</p>

<p>The <code>IPrintOemUni::SendFontCmd</code> method is optional. If a rendering plug-in implements this method, the plug-in's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554253">IPrintOemUni::GetImplementedMethod</a> method must return S_OK when it receives "SendFontCmd" as input.</p>

<p>For additional information see <a href="NULL">Customized Font Management</a>.</p>

<p>The <code>IPrintOemUni::SendFontCmd</code> method is used for selecting device fonts on printers that do not recognize the <a href="wdkgloss.p#wdkgloss.pcl#wdkgloss.pcl"><i>PCL</i></a>, CAPSL, or PPDS-formatted font commands supported by Unidrv. Its purpose is to allow a rendering plug-in to modify the font selection command that is specified in the font's .ufm (Unidrv Font Metrics) file. (To see how the command is stored, refer to the description of .ufm file's <a href="https://msdn.microsoft.com/library/windows/hardware/ff562872">UNIDRVINFO</a> structure.) If the command needs to be modified before being sent to the printer, you should implement the <code>IPrintOemUni::SendFontCmd</code> method.</p>

<p>The method receives the command string in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548846">FINVOCATION</a> structure pointed to by <i>pFInv</i>. Typically, the string contains variables for which values must be supplied. For example, the following font selection command requires that <i>#FontHeight</i> and <i>#FontWidth</i> be replaced with numeric values:</p>

<p>Current values for the font height and width can be obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff563594">UNIFONTOBJ_GetInfo</a> to read Unidrv's standard variables.</p>

<p>Whenever the <code>IPrintOemUni::SendFontCmd</code> method called, it must send the command string to the printer by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff553138">IPrintOemDriverUni::DrvWriteSpoolBuf</a>.</p>

<p>The <code>IPrintOemUni::SendFontCmd</code> method is optional. If a rendering plug-in implements this method, the plug-in's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554253">IPrintOemUni::GetImplementedMethod</a> method must return S_OK when it receives "SendFontCmd" as input.</p>

<p>For additional information see <a href="NULL">Customized Font Management</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547573">DEVOBJ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563590">UNIFONTOBJ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548846">FINVOCATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563594">UNIFONTOBJ_GetInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553138">IPrintOemDriverUni::DrvWriteSpoolBuf</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554253">IPrintOemUni::GetImplementedMethod</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUni::SendFontCmd method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
