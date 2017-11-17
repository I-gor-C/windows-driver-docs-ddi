---
UID: NS.winbio_ioctl._WINBIO_CAPTURE_PARAMETERS
title: WINBIO_CAPTURE_PARAMETERS
author: windows-driver-content
description: The IOCTL_BIOMETRIC_CAPTURE_DATA IOCTL uses the WINBIO_CAPTURE_PARAMETERS structure as input.
old-location: biometric\winbio_capture_parameters.htm
ms.assetid: 60f35000-c62d-4d1b-8592-862c2d74b7a2
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: biometric
req.header: winbio_ioctl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WINBIO_CAPTURE_PARAMETERS
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
ms.keywords: WINBIO_CAPTURE_PARAMETERS, WINBIO_CAPTURE_PARAMETERS, *PWINBIO_CAPTURE_PARAMETERS
req.iface: 
req.product: Windows 10 or later.
---

# WINBIO_CAPTURE_PARAMETERS structure



## -description
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff536429">IOCTL_BIOMETRIC_CAPTURE_DATA</a> IOCTL uses the WINBIO_CAPTURE_PARAMETERS structure as input.</p>


## -syntax

````
typedef struct _WINBIO_CAPTURE_PARAMETERS {
  DWORD                    PayloadSize;
  WINBIO_BIR_PURPOSE       Purpose;
  WINBIO_REGISTERED_FORMAT Format;
  WINBIO_UUID              VendorFormat;
  WINBIO_BIR_DATA_FLAGS    Flags;
} WINBIO_CAPTURE_PARAMETERS, *PWINBIO_CAPTURE_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>PayloadSize</b>

<dd>
<p>The total size of the payload.</p>
</dd>

### -field <b>Purpose</b>

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff536463">WINBIO_BIR_PURPOSE</a> reason for the data collection.  Some sensors will go into a different mode depending on the reason for the data capture.</p>
</dd>

### -field <b>Format</b>

<dd>
<p>Specifies the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536473">WINBIO_REGISTERED_FORMAT</a> format of the data to be returned.</p>
</dd>

### -field <b>VendorFormat</b>

<dd>
<p>An optional <a href="https://msdn.microsoft.com/library/windows/hardware/ff536480">WINBIO_UUID</a> vendor GUID.  This indicates the preferred format of the vendor-specific data in the BIR.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Specifies the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536461">WINBIO_BIR_DATA_FLAGS</a> level of processing and other attributes for the data to be returned.  If format owner and type are the Windows standard, this must be WINBIO_DATA_FLAG_RAW.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536429">IOCTL_BIOMETRIC_CAPTURE_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [biometric\biometric]:%20WINBIO_CAPTURE_PARAMETERS structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
