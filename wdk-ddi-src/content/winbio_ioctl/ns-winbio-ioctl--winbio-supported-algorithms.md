---
UID: NS.winbio_ioctl._WINBIO_SUPPORTED_ALGORITHMS
title: WINBIO_SUPPORTED_ALGORITHMS
author: windows-driver-content
description: The WINBIO_SUPPORTED_ALGORITHMS structure is the OUT payload for IOCTL_BIOMETRIC_GET_SUPPORTED_ALGORITHMS.
old-location: biometric\winbio_supported_algorithms.htm
old-project: biometric
ms.assetid: cb2236f6-409a-4352-a02b-f7763e986d1f
ms.author: windowsdriverdev
ms.date: 11/13/2017
ms.keywords: WINBIO_SUPPORTED_ALGORITHMS, WINBIO_SUPPORTED_ALGORITHMS, *PWINBIO_SUPPORTED_ALGORITHMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: winbio_ioctl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WINBIO_SUPPORTED_ALGORITHMS
req.alt-loc: winbio_ioctl.h
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
req.iface: IWiaTransferCallback
req.product: Windows 10 or later.
---

# WINBIO_SUPPORTED_ALGORITHMS structure



## -description
<p>The WINBIO_SUPPORTED_ALGORITHMS structure is the OUT payload for <a href="https://msdn.microsoft.com/library/windows/hardware/ff536438">IOCTL_BIOMETRIC_GET_SUPPORTED_ALGORITHMS</a>.</p>


## -syntax

````
typedef struct _WINBIO_SUPPORTED_ALGORITHMS {
  DWORD       PayloadSize;
  HRESULT     WinBioHresult;
  DWORD       NumberOfAlgorithms;
  WINBIO_DATA AlgorithmData;
} WINBIO_SUPPORTED_ALGORITHMS, *PWINBIO_SUPPORTED_ALGORITHMS;
````


## -struct-fields
<dl>

### -field <b>PayloadSize</b>

<dd>
<p>Specifies the total size of the payload, which includes the fixed length structure and any variable data at the end.</p>
</dd>

### -field <b>WinBioHresult</b>

<dd>
<p>Specifies the HRESULT status of the I/O operation.</p>
</dd>

### -field <b>NumberOfAlgorithms</b>

<dd>
<p>Specifies the number of algorithms in the data block.</p>
</dd>

### -field <b>AlgorithmData</b>

<dd>
<p>Specifies a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff536469">WINBIO_DATA</a> that contains NULL-terminated UTF-8 OID strings that represent the algorithms supported by the device.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winbio_ioctl.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536438">IOCTL_BIOMETRIC_GET_SUPPORTED_ALGORITHMS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [biometric\biometric]:%20WINBIO_SUPPORTED_ALGORITHMS structure%20 RELEASE:%20(11/13/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
