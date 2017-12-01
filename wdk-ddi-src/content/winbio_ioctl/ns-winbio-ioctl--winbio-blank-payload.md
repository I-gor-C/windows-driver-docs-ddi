---
UID: NS.winbio_ioctl._WINBIO_BLANK_PAYLOAD
title: WINBIO_BLANK_PAYLOAD
author: windows-driver-content
description: The IOCTL_BIOMETRIC_RESET and IOCTL_BIOMETRIC_UPDATE_FIRMWARE IOCTLs return the WINBIO_BLANK_PAYLOAD structure as output.
old-location: biometric\winbio_blank_payload.htm
old-project: biometric
ms.assetid: 0bc28853-1c00-42d3-a269-198093d64dd7
ms.author: windowsdriverdev
ms.date: 11/13/2017
ms.keywords: WINBIO_BLANK_PAYLOAD, WINBIO_BLANK_PAYLOAD, *PWINBIO_BLANK_PAYLOAD
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
req.alt-api: WINBIO_BLANK_PAYLOAD
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

# WINBIO_BLANK_PAYLOAD structure



## -description
<p>The <a href="..\winbio_ioctl\ni-winbio-ioctl-ioctl-biometric-reset.md">IOCTL_BIOMETRIC_RESET</a> and <a href="..\winbio_ioctl\ni-winbio-ioctl-ioctl-biometric-update-firmware.md">IOCTL_BIOMETRIC_UPDATE_FIRMWARE</a> IOCTLs return the WINBIO_BLANK_PAYLOAD structure as output.</p>


## -syntax

````
typedef struct _WINBIO_BLANK_PAYLOAD {
  DWORD   PayloadSize;
  HRESULT WinBioHresult;
} WINBIO_BLANK_PAYLOAD, *PWINBIO_BLANK_PAYLOAD;
````


## -struct-fields
<dl>

### -field <b>PayloadSize</b>

<dd>
<p> The total size of the payload.  This includes the fixed length structure and any variable data at the end.</p>
</dd>

### -field <b>WinBioHresult</b>

<dd>
<p>The status detail of the I/O operation.  This is where WINBIO error and information codes will be passed. The following table shows possible values.</p>
<table>
<tr>
<th>Status value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>S_OK</p>
</td>
<td>
<p>The operation completed successfully.</p>
</td>
</tr>
<tr>
<td>
<p>HRESULT_FROM_NT(STATUS_IO_DEVICE_ERROR)</p>
</td>
<td>
<p>The driver could not gather the necessary information from the device.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_E_DEVICE_BUSY</p>
</td>
<td>
<p>The device is in the middle of a vendor-specific operation.  This should only be returned when the device cannot be reset, and the vendor-specific operation cannot be canceled.</p>
</td>
</tr>
</table>
<p> </p>
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