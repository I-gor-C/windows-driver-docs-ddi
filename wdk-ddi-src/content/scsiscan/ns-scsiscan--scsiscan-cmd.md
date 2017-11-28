---
UID: NS.scsiscan._SCSISCAN_CMD
title: SCSISCAN_CMD
author: windows-driver-content
description: The SCSISCAN_CMD structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_SCSISCAN_CMD.
old-location: image\scsiscan_cmd.htm
old-project: image
ms.assetid: 412c35b2-eb08-43a3-b776-053645806f5d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: SCSISCAN_CMD, SCSISCAN_CMD, *PSCSISCAN_CMD
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: scsiscan.h
req.include-header: Scsiscan.h, Srb.h, Scsi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SCSISCAN_CMD
req.alt-loc: scsiscan.h
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
req.product: Windows 10 or later.
---

# SCSISCAN_CMD structure



## -description
<p>The SCSISCAN_CMD structure is used as a parameter to <a href="base.deviceiocontrol">DeviceIoControl</a>, when the specified I/O control code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff542877">IOCTL_SCSISCAN_CMD</a>.</p>


## -syntax

````
typedef struct _SCSISCAN_CMD {
  ULONG  Reserved1;
  ULONG  Size;
  ULONG  SrbFlags;
  UCHAR  CdbLength;
  UCHAR  SenseLength;
  UCHAR  Reserved2;
  UCHAR  Reserved3;
  ULONG  TransferLength;
  UCHAR  Cdb[16];
  PUCHAR pSrbStatus;
  PUCHAR pSenseBuffer;
} SCSISCAN_CMD, *PSCSISCAN_CMD;
````


## -struct-fields
<dl>

### -field <b>Reserved1</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Caller-supplied size, in bytes, of the SCSISCAN_CMD structure.</p>
</dd>

### -field <b>SrbFlags</b>

<dd>
<p>Caller-supplied SRB_FLAGS-prefixed bit flag specifying the requested operation. Flags are defined in <i>srb.h</i>.</p>
</dd>

### -field <b>CdbLength</b>

<dd>
<p>Length, in bytes, of the <a href="wdkgloss.c#wdkgloss.cdb#wdkgloss.cdb"><i>CDB</i></a> contained in the <b>Cdb</b> member.</p>
</dd>

### -field <b>SenseLength</b>

<dd>
<p>Length, in bytes, of the sense buffer the <b>pSenseBuffer</b> member points to.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>Reserved3</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>TransferLength</b>

<dd>
<p>Length, in bytes, of the buffer to be transferred. This should match the value specified for the <a href="base.deviceiocontrol">DeviceIoControl</a> function's <i>nOutBufferSize</i> parameter.</p>
</dd>

### -field <b>Cdb</b>

<dd>
<p>Caller-supplied <a href="wdkgloss.c#wdkgloss.cdb#wdkgloss.cdb"><i>CDB</i></a> data. (The CDB structure is declared in <i>scsi.h</i>.)</p>
</dd>

### -field <b>pSrbStatus</b>

<dd>
<p>Caller-supplied pointer that will receive one of the SRB_STATUS-prefixed status values defined in <i>srb.h</i>.</p>
</dd>

### -field <b>pSenseBuffer</b>

<dd>
<p>Caller-supplied pointer to a request-sense buffer, to be filled in by the kernel-mode driver.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Scsiscan.h (include Scsiscan.h, Srb.h, or Scsi.h)</dt>
</dl>
</td>
</tr>
</table>