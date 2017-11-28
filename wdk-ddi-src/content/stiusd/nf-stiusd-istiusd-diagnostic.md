---
UID: NF.stiusd.IStiUSD.Diagnostic
title: IStiUSD::Diagnostic
author: windows-driver-content
description: A still image minidriver's IStiUSD::Diagnostic method runs diagnostic tests on a still image device.
old-location: image\istiusd_diagnostic.htm
old-project: image
ms.assetid: bf99c34e-5a71-4f2b-8dca-bed87d18b352
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IStiUSD, Diagnostic, IStiUSD::Diagnostic
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: stiusd.h
req.include-header: Stiusd.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IStiUSD.Diagnostic
req.alt-loc: stiusd.h
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
req.iface: IStiUSD
req.product: Windows 10 or later.
---

# IStiUSD::Diagnostic method



## -description
<p>A still image minidriver's <b>IStiUSD::Diagnostic</b> method runs diagnostic tests on a still image device.</p>


## -syntax

````
HRESULT Diagnostic(
   LPSTI_DIAG pBuffer
);
````


## -parameters
<dl>

### -param <i>pBuffer</i> 

<dd>
<p>Caller-supplied pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548383">STI_DIAG</a> structure to receive testing status information.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method should return S_OK. Otherwise, it should return one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>The <b>IStiUSD::Diagnostic</b> method is called when a user clicks on the Scanners and Cameras Control Panel's Test button. The method should execute tests to confirm that the device is fully operational. For a scanner, these tests might include turning the light on and off, and moving the scanning arm. For a camera, they might include execution of built-in diagnostic functions, or manipulation of device settings. The return value should indicate success or failure of the diagnostic tests.</p>

<p>The <b>IStiUSD::Diagnostic</b> method is called when a user clicks on the Scanners and Cameras Control Panel's Test button. The method should execute tests to confirm that the device is fully operational. For a scanner, these tests might include turning the light on and off, and moving the scanning arm. For a camera, they might include execution of built-in diagnostic functions, or manipulation of device settings. The return value should indicate success or failure of the diagnostic tests.</p>

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
<dt>Stiusd.h (include Stiusd.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543736">IStiDevice::Diagnostic</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IStiUSD::Diagnostic method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
