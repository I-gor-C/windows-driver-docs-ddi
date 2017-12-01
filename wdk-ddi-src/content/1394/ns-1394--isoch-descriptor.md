---
UID: NS.1394._ISOCH_DESCRIPTOR
title: ISOCH_DESCRIPTOR
author: windows-driver-content
description: The ISOCH_DESCRIPTOR structure describes a buffer to be attached or detailed from a resource handle, using the REQUEST_ISOCH_ATTACH_BUFFERS and REQUEST_ISOCH_DETACH_BUFFERS requests.
old-location: ieee\isoch_descriptor.htm
old-project: IEEE
ms.assetid: 4f508af6-942b-4d48-8874-4b6d9918f01f
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: ISOCH_DESCRIPTOR, ISOCH_DESCRIPTOR, *PISOCH_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 1394.h
req.include-header: 1394.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ISOCH_DESCRIPTOR
req.alt-loc: 1394.h
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
---

# ISOCH_DESCRIPTOR structure



## -description
<p>The ISOCH_DESCRIPTOR structure describes a buffer to be attached or detailed from a resource handle, using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537650">REQUEST_ISOCH_ATTACH_BUFFERS</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff537651">REQUEST_ISOCH_DETACH_BUFFERS</a> requests.</p>


## -syntax

````
typedef struct _ISOCH_DESCRIPTOR {
  ULONG                         fulFlags;
  PMDL                          Mdl;
  ULONG                         ulLength;
  ULONG                         nMaxBytesPerFrame;
  ULONG                         ulSynch;
  ULONG                         ulTag;
  CYCLE_TIME                    CycleTime;
  PBUS_ISOCH_DESCRIPTOR_ROUTINE Callback;
  PVOID                         Context1;
  PVOID                         Context2;
  NTSTATUS                      status;
  ULONG_PTR                     DeviceReserved[8];
  ULONG_PTR                     BusReserved[8];
  ULONG_PTR                     PortReserved[16];
} ISOCH_DESCRIPTOR, *PISOCH_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>fulFlags</b>

<dd>
<p>Specifies various flags for this isochronous descriptor. Each attached buffer on the channel has an associated isoch descriptor. </p>
<p>Before using a particular buffer for an I/O operation, the host controller examines the flags in the buffer's isoch descriptor for instructions on how to handle the data. In some cases, the host controller will continue to observe the behavior specified by these flags during I/O operations with subsequent buffers. For instance, if the isoch descriptor flags indicate that the host controller should filter out packets that do not have a certain Sy value recorded in <b>ulSynch</b>, the host controller will continue this filtering operation with the data in the buffers that follow, even if the isoch descriptors associated with these buffers do not have the same flags set. </p>
<p>The following table describes the flags that can be assigned to this member.</p>
<table>
<tr>
<th>Flag</th>
<th>Isochronous Transaction</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DESCRIPTOR_SYNCH_ON_SY </p>
</td>
<td>
<p>Listen</p>
</td>
<td>
<p>Starting with the data in current buffer, the host controller ignores all packets not containing a particular Sy value that is embedded in the isochronous packet. The Sy value is specified in <b>ulSynch</b>. If the DESCRIPTOR_USE_SY_TAG_IN_FIRST flag is set, the host controller resumes reading all packets after encountering the first packet with the Sy value specified in <b>ulSynch</b>. If the DESCRIPTOR_USE_SY_TAG_IN_FIRST flag is not set, the host controller continues filtering, reading packets with the indicated Sy value and ignoring all others. </p>
</td>
</tr>
<tr>
<td>
<p>DESCRIPTOR_SYNCH_ON_TAG </p>
</td>
<td>
<p>Listen</p>
</td>
<td>
<p>Starting with the data in current buffer, the host controller ignores all packets not containing a particular tag value that is embedded in the isochronous packet. The tag value is specified in <b>ulTag</b>. If the DESCRIPTOR_USE_SY_TAG_IN_FIRST flag is set, the host controller resumes reading all packets after encountering the first packet with the tag value specified in <b>ulTag</b>. If the DESCRIPTOR_USE_SY_TAG_IN_FIRST flag is not set, the host controller continues filtering, reading packets with the indicated tag value and ignoring all others. </p>
</td>
</tr>
<tr>
<td>
<p>DESCRIPTOR_SYNCH_ON_TIME</p>
</td>
<td>
<p>Listen, Talk</p>
</td>
<td>
<p>The host controller waits for a particular isochronous cycle time before continuing the operation. The cycle time is specified in the <b>CycleTime</b> member. Starting with the data in the current buffer, the host controller ignores all packets not containing a cycle time of <b>CycleTime</b>. After finding a packet with the indicated cycle time, the host controller resumes processing all packets. </p>
</td>
</tr>
<tr>
<td>
<p>DESCRIPTOR_USE_SY_TAG_IN_FIRST</p>
</td>
<td>
<p>Listen</p>
</td>
<td>
<p>Filtering on the <b>Sy</b> or <b>Tag</b> members occurs only until the first matching packet is received. This flag is used in conjunction with the flags DESCRIPTOR_SYNCH_ON_SY and DESCRIPTOR_SYNCH_ON_TAG. These two flags initiate a filtering operation based on the values in <b>Sy</b> or <b>Tag</b>, unless DESCRIPTOR_USE_SY_TAG_IN_FIRST is also set, in which case these flags initiate a synchronization rather than a filtering operation. In this synchronization operation the host controller ignores all packets until discovering a packet with the right <b>Sy</b> or <b>Tag</b> value. After discovering a packet with the indicated <b>Sy</b> or <b>Tag</b> value, the host controller resumes processing all packets. </p>
</td>
</tr>
<tr>
<td>
<p>DESCRIPTOR_TIME_STAMP_ON_COMPLETION</p>
</td>
<td>
<p>Listen, Talk</p>
</td>
<td>
<p>Once the host controller completes its DMA to or from this buffer, store the cycle time in the <b>CycleTime</b> member of the ISOCH_DESCRIPTOR.</p>
</td>
</tr>
<tr>
<td>
<p>DESCRIPTOR_PRIORITY_TIME_DELIVERY</p>
</td>
<td>
<p>Talk</p>
</td>
<td>
<p>If the local host controller is not ready for a write, do not retry the write later. (The default behavior is to retry until the host controller is ready.)</p>
</td>
</tr>
<tr>
<td>
<p>DESCRIPTOR_HEADER_SCATTER_GATHER</p>
</td>
<td>
<p>Talk</p>
</td>
<td>
<p>The host controller treats the data in this buffer as a sequence of headers. The host controller prepends a header from this buffer to each packet it assembles from the data in the next buffer attached.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Mdl</b>

<dd>
<p>Specifies the MDL representing a buffer in which the data is, or will be, contained. </p>
</dd>

### -field <b>ulLength</b>

<dd>
<p>Specifies the length of the <b>Mdl</b>.</p>
</dd>

### -field <b>nMaxBytesPerFrame</b>

<dd>
<p>Specifies the maximum bytes contained in each isochronous frame. On writes, the data in the buffer is split into isochronous packets of this size.</p>
</dd>

### -field <b>ulSynch</b>

<dd>
<p>For IsochTalk requests, if the DESCRIPTOR_SYNCH_ON_SY flag is set, this member specifies the Sy field of the outgoing packet. For REQUEST_ISOCH_LISTEN requests, if the DESCRIPTOR_SYNCH_ON_SY flag is set, this member specifies the value the host controller will match against the Sy field in isochronous packet headers.</p>
</dd>

### -field <b>ulTag</b>

<dd>
<p>For IsochTalk requests, this member specifies the Tag field of the outgoing packet. For REQUEST_ISOCH_LISTEN requests, if the DESCRIPTOR_SYNCH_ON_TAG flag is set, this member specifies the value the host controller will match against the Tag field in isochronous packet headers.</p>
</dd>

### -field <b>CycleTime</b>

<dd>
<p>If the DESCRIPTOR_SYNCH_ON_TIME flag is set, this member specifies the isochronous cycle time to synchronize on. (The timing resolution is per isochronous cycle. The <b>CycleOffset</b> member of the cycle time is not used.) If the DESCRIPTOR_TIME_STAMP_ON_COMPLETION flag is set, the bus driver fills this member with the isochronous cycle time on completion of the operation that used this buffer.</p>
</dd>

### -field <b>Callback</b>

<dd>
<p>Pointer to a callback routine. If non-NULL, the bus driver calls this routine to indicate that the associated attached buffers are ready to be detached. The callback executes at IRQL DISPATCH_LEVEL. The callback is of the following type:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>void Callback(IN PVOID Context1, IN PVOID Context2);</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>Context1</b>

<dd>
<p>Specifies the first parameter when the bus driver calls the routine passed in <b>Callback</b>.</p>
</dd>

### -field <b>Context2</b>

<dd>
<p>Specifies the second parameter when the bus driver calls the routine passed in <b>Callback</b>.</p>
</dd>

### -field <b>status</b>

<dd>
<p>For <a href="https://msdn.microsoft.com/library/windows/hardware/ff537650">REQUEST_ISOCH_ATTACH_BUFFERS</a> requests, this member specifies the status of the attach operation on this buffer.   If an error occurs during the processing of the <b>REQUEST_ISOCH_ATTACH_BUFFERS</b> request, the bus driver fills in the <b>status</b> member with an appropriate error code.
</p>
<div class="alert"><b>Note</b>  The <b>status</b> member must be initialized to STATUS_SUCCESS before the <b>REQUEST_ISOCH_ATTACH_BUFFERS</b> request is made.</div>
<div> </div>
</dd>

### -field <b>DeviceReserved</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>BusReserved</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>PortReserved</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>

## -remarks
<p>Not all DESCRIPTOR_XXX flags are supported on all hardware. The device driver can use the REQUEST_GET_LOCAL_HOST_INFO request, with <b>nLevel</b> = GET_HOST_CAPABILITIES, to determine which DESCRIPTOR_XXX flags are supported. The bus driver returns a pointer to a GET_LOCAL_HOST_INFO2 structure, whose <b>HostCapabilities</b> member contains flags that determine which flags the host controller supports. The following table lists which DESCRIPTOR_XXX flags require hardware support, and the corresponding <b>HostCapabilities</b> flag the driver should check.</p>

<p>DESCRIPTOR_SYNCH_ON_TIME</p>

<p>HOST_INFO_SUPPORTS_START_ON_CYCLE</p>

<p>DESCRIPTOR_HEADER_SCATTER_GATHER</p>

<p>HOST_INFO_SUPPORTS_ISO_HDR_INSERTION</p>

<p>If the driver sets the DESCRIPTOR_HEADER_SCATTER_GATHER flag, the host controller combines the data of the buffer specified in <b>Mdl</b> with the data of the next buffer attached. (Subsequent buffers are unaffected.) Each frame of the buffer is prepended to a frame of the next buffer (in the order the data in the buffer is split into frames), and sent as the data of the next isochronous packet. The number of frames of each buffer must match, or the bus driver returns STATUS_INVALID_PARAMETER for the next REQUEST_ISOCH_ATTACH_BUFFER request.</p>

<p>The DESCRIPTOR_HEADER_SCATTER_GATHER flag is not supported on Windows 98/Me. It is supported on Windows 2000 and later operating systems.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>1394.h (include 1394.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537651">REQUEST_ISOCH_DETACH_BUFFERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537660">REQUEST_ISOCH_TALK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537147">GET_LOCAL_HOST_INFO2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537649">REQUEST_ISOCH_ALLOCATE_RESOURCES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537650">REQUEST_ISOCH_ATTACH_BUFFERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537655">REQUEST_ISOCH_LISTEN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20ISOCH_DESCRIPTOR structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
