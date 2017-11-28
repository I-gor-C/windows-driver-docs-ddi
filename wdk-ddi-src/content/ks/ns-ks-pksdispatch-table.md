---
UID: NS.ks.PKSDISPATCH_TABLE
title: PKSDISPATCH_TABLE
author: windows-driver-content
description: The KSDISPATCH_TABLE structure contains pointers to minidriver implemented IRP dispatch routines.
old-location: stream\ksdispatch_table.htm
old-project: stream
ms.assetid: baa45ce7-3dcd-4383-99f2-aeb664a03190
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSDISPATCH_TABLE, KSDISPATCH_TABLE, *PKSDISPATCH_TABLE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSDISPATCH_TABLE
req.alt-loc: ks.h
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

# PKSDISPATCH_TABLE structure



## -description
<p>The KSDISPATCH_TABLE structure contains pointers to minidriver implemented IRP dispatch routines.</p>


## -syntax

````
typedef struct {
  PDRIVER_DISPATCH        DeviceIoControl;
  PDRIVER_DISPATCH        Read;
  PDRIVER_DISPATCH        Write;
  PDRIVER_DISPATCH        Flush;
  PDRIVER_DISPATCH        Close;
  PDRIVER_DISPATCH        QuerySecurity;
  PDRIVER_DISPATCH        SetSecurity;
  PFAST_IO_DEVICE_CONTROL FastDeviceIoControl;
  PFAST_IO_READ           FastRead;
  PFAST_IO_WRITE          FastWrite;
} KSDISPATCH_TABLE, *PKSDISPATCH_TABLE;
````


## -struct-fields
<dl>

### -field <b>DeviceIoControl</b>

<dd>
<p>Specifies the minidriver's routine to dispatch <a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a> IRPs to.</p>
</dd>

### -field <b>Read</b>

<dd>
<p>Specifies the minidriver's routine to dispatch <a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a> IRPs to.</p>
</dd>

### -field <b>Write</b>

<dd>
<p>Specifies the minidriver's routine to dispatch <a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a> IRPs to.</p>
</dd>

### -field <b>Flush</b>

<dd>
<p>Specifies the minidriver's routine to dispatch <a href="https://msdn.microsoft.com/library/windows/hardware/ff549235">IRP_MJ_FLUSH_BUFFERS</a> IRPs to.</p>
</dd>

### -field <b>Close</b>

<dd>
<p>Specifies the minidriver's routine to dispatch <a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a> IRPs to.</p>
</dd>

### -field <b>QuerySecurity</b>

<dd>
<p>Specifies the minidriver's routine to dispatch <a href="https://msdn.microsoft.com/library/windows/hardware/ff549298">IRP_MJ_QUERY_SECURITY</a> IRPs to.</p>
</dd>

### -field <b>SetSecurity</b>

<dd>
<p>Specifies the minidriver's routine to dispatch <a href="https://msdn.microsoft.com/library/windows/hardware/ff549407">IRP_MJ_SET_SECURITY</a> IRPs to.</p>
</dd>

### -field <b>FastDeviceIoControl</b>

<dd>
<p>Specifies the minidriver's routine to dispatch fast device I/O control requests to.</p>
</dd>

### -field <b>FastRead</b>

<dd>
<p>Specifies the minidriver's routine to dispatch fast read requests to.</p>
</dd>

### -field <b>FastWrite</b>

<dd>
<p>Specifies the minidriver's routine to dispatch fast write requests to.</p>
</dd>
</dl>

## -remarks
<p>A pointer to a dispatch table is contained in the opaque object header that is the first element of data pointed to by the file object's <b>FsContext</b> field.</p>

<p>For more information about minidriver implemented IRP dispatch routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff566840">KsSetMajorFunctionHandler</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566840">KsSetMajorFunctionHandler</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSDISPATCH_TABLE structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
