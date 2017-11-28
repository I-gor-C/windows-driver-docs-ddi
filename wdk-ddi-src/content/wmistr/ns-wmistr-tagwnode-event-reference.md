---
UID: NS.wmistr.tagWNODE_EVENT_REFERENCE
title: tagWNODE_EVENT_REFERENCE
author: windows-driver-content
description: The WNODE_EVENT_REFERENCE structure contains information that WMI can use to query for an event that exceeds the event size limit set in the registry.
old-location: kernel\wnode_event_reference.htm
old-project: kernel
ms.assetid: 9dfe75e5-301e-4378-a2ad-f43676d8c208
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: tagWNODE_EVENT_REFERENCE, WNODE_EVENT_REFERENCE, *PWNODE_EVENT_REFERENCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wmistr.h
req.include-header: Wmistr.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WNODE_EVENT_REFERENCE
req.alt-loc: Wmistr.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# tagWNODE_EVENT_REFERENCE structure



## -description
<p>The <b>WNODE_EVENT_REFERENCE</b> structure contains information that WMI can use to query for an event that exceeds the event size limit set in the registry.</p>


## -syntax

````
typedef struct tagWNODE_EVENT_REFERENCE {
  struct _WNODE_HEADER  WnodeHeader;
  GUID                 TargetGuid;
  ULONG                TargetDataBlockSize;
  union {
    ULONG TargetInstanceIndex;
    WCHAR TargetInstanceName[];
  };
} WNODE_EVENT_REFERENCE, *PWNODE_EVENT_REFERENCE;
````


## -struct-fields
<dl>

### -field <b>WnodeHeader</b>

<dd>
<p>Is a <a href="https://msdn.microsoft.com/library/windows/hardware/ff566375">WNODE_HEADER</a> structure that contains information common to all <b>WNODE_<i>XXX</i></b> structures, such as the buffer size, the provider ID, the GUID that represents a data block associated with a request, and flags that provide information about the <b>WNODE_<i>XXX</i></b> data being passed or returned.</p>
</dd>

### -field <b>TargetGuid</b>

<dd>
<p>Indicates the GUID that represents the event to query.</p>
</dd>

### -field <b>TargetDataBlockSize</b>

<dd>
<p>Indicates the size of the event.</p>
</dd>

### -field <b>TargetInstanceIndex</b>

<dd>
<p>Indicates the index into the driver's list of static instance names for the event. This member is valid only if the event block was registered with static instance names and WNODE_FLAGS_STATIC_INSTANCE_NAMES is set in <b>WnodeHeader.Flags</b>.</p>
</dd>

### -field <b>TargetInstanceName</b>

<dd>
<p>Indicates the dynamic instance name of the event as a counted Unicode string. This member is valid only if WNODE_FLAGS_STATIC_INSTANCE_NAMES is clear in <b>WnodeHeader.Flags</b> and the event block was registered with dynamic instance names.</p>
</dd>
</dl>

## -remarks
<p>If the amount of data for an event exceeds the maximum size set in the registry, a driver can generate a <b>WNODE_EVENT_REFERENCE</b> that specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff566373">WNODE_EVENT_ITEM</a> that WMI can query to obtain the event. For more information about defining and generating WMI events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff547139">Implementing WMI</a>.</p>

<p>The <b>ProviderId</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566375">WNODE_HEADER</a> structure for use in a <b>WNODE_EVENT_REFERENCE</b> structure should be initialized using <a href="https://msdn.microsoft.com/library/windows/hardware/ff550433">IoWMIDeviceObjectToProviderId</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wmistr.h (include Wmistr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566373">WNODE_EVENT_ITEM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566375">WNODE_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550433">IoWMIDeviceObjectToProviderId</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20WNODE_EVENT_REFERENCE structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
