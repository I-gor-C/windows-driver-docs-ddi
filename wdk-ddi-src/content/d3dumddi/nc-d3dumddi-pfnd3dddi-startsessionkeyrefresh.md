---
UID: NC.d3dumddi.PFND3DDDI_STARTSESSIONKEYREFRESH
title: PFND3DDDI_STARTSESSIONKEYREFRESH
author: windows-driver-content
description: The StartSessionKeyRefresh function returns a random number that the driver's FinishSessionKeyRefresh function subsequently uses to perform an exclusive OR operation (XOR) with the session key.
old-location: display\startsessionkeyrefresh.htm
old-project: display
ms.assetid: 986d8f46-3b4f-41b2-938e-4f3adbfe057a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: StartSessionKeyRefresh is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StartSessionKeyRefresh
req.alt-loc: d3dumddi.h
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
---

# PFND3DDDI_STARTSESSIONKEYREFRESH callback



## -description
<p>The <i>StartSessionKeyRefresh</i> function returns a random number that the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451648">FinishSessionKeyRefresh</a> function subsequently uses to perform an exclusive OR operation (XOR) with the session key. </p>


## -prototype

````
PFND3DDDI_STARTSESSIONKEYREFRESH StartSessionKeyRefresh;

__checkReturn HRESULT APIENTRY StartSessionKeyRefresh(
  _In_          HANDLE                           hDevice,
  _Inout_ const D3DDDIARG_STARTSESSIONKEYREFRESH *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in, out]

<dd>
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543375">D3DDDIARG_STARTSESSIONKEYREFRESH</a> structure that contains information about the random number. </p>
</dd>
</dl>

## -returns
<p><i>StartSessionKeyRefresh</i> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The random number is successfully returned. </p><dl>
<dt><b>D3DDDIERR_NOTAVAILABLE</b></dt>
</dl><p>The driver does not support the <i>StartSessionKeyRefresh</i> function. </p>

<p> </p>

## -remarks
<p>The hardware and driver can optionally support <i>StartSessionKeyRefresh</i> for all crypto types.  </p>

<p>When the Direct3D runtime calls the driver's <i>StartSessionKeyRefresh</i> function, the driver generates and saves a random number and returns the random number in the buffer that the <b>pRandomNumber</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543375">D3DDDIARG_STARTSESSIONKEYREFRESH</a> structure points to.</p>

<p>When the runtime subsequently calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451648">FinishSessionKeyRefresh</a> function, the driver performs an XOR operation of the random number with the session key.</p>

<p>The hardware and driver can optionally support <i>StartSessionKeyRefresh</i> for all crypto types.  </p>

<p>When the Direct3D runtime calls the driver's <i>StartSessionKeyRefresh</i> function, the driver generates and saves a random number and returns the random number in the buffer that the <b>pRandomNumber</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543375">D3DDDIARG_STARTSESSIONKEYREFRESH</a> structure points to.</p>

<p>When the runtime subsequently calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451648">FinishSessionKeyRefresh</a> function, the driver performs an XOR operation of the random number with the session key.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p><i>StartSessionKeyRefresh</i> is supported beginning with the Windows 7 operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543375">D3DDDIARG_STARTSESSIONKEYREFRESH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451648">FinishSessionKeyRefresh</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_STARTSESSIONKEYREFRESH callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
