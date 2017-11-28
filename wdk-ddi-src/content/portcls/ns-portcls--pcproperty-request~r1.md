---
UID: NS.portcls._PCPROPERTY_REQUEST~r1
title: PCPROPERTY_REQUEST
author: windows-driver-content
description: The PCPROPERTY_REQUEST structure specifies a property request.
old-location: audio\pcproperty_request.htm
old-project: audio
ms.assetid: 3683735d-ce00-4615-9782-dee9f4753cc7
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PCPROPERTY_REQUEST,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PCPROPERTY_REQUEST
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PCPROPERTY_REQUEST structure



## -description
<p>The <b>PCPROPERTY_REQUEST</b> structure specifies a property request.</p>


## -syntax

````
typedef struct _PCPROPERTY_REQUEST {
  PUNKNOWN              MajorTarget;
  PUNKNOWN              MinorTarget;
  ULONG                 Node;
  const PCPROPERTY_ITEM *PropertyItem;
  ULONG                 Verb;
  ULONG                 InstanceSize;
  PVOID                 Instance;
  ULONG                 ValueSize;
  PVOID                 Value;
  PIRP                  Irp;
} PCPROPERTY_REQUEST, *PPCPROPERTY_REQUEST;
````


## -struct-fields
<dl>

### -field <b>MajorTarget</b>

<dd>
<p>
<a href="com.iunknown">IUnknown</a> pointer to the main miniport object. This member contains the <i>UnknownMiniport</i> parameter value that the adapter driver previously passed to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536943">IPort::Init</a> method.</p>
</dd>

### -field <b>MinorTarget</b>

<dd>
<p>
<a href="com.iunknown">IUnknown</a> pointer to a stream object that is associated with the <b>MajorTarget</b> miniport object. If the target for the property request is a pin instance, this member contains the stream-object pointer that the IMiniport <i>Xxx</i>::NewStream method previously output to the port driver (for example, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536723">IMiniportWaveCyclic::NewStream</a> method's <i>Stream</i> parameter). Otherwise (if the target for the property request is a filter instance), this member is <b>NULL</b>.</p>
</dd>

### -field <b>Node</b>

<dd>
<p>Specifies a node ID. This member identifies the target node for the request. If the target is not a node, this member is set to ULONG(-1).</p>
</dd>

### -field <b>PropertyItem</b>

<dd>
<p>Pointer to the property item, which is a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff537722">PCPROPERTY_ITEM</a>.</p>
</dd>

### -field <b>Verb</b>

<dd>
<p>Specifies the type of property request. <b>Verb</b> is set to the bitwise OR of one or more of the following flag bits from header file ks.h:</p>
<ul>
<li>
<p>KSPROPERTY_TYPE_GET</p>
</li>
<li>
<p>KSPROPERTY_TYPE_SET</p>
</li>
<li>
<p>KSPROPERTY_TYPE_SETSUPPORT</p>
</li>
<li>
<p>KSPROPERTY_TYPE_BASICSUPPORT</p>
</li>
<li>
<p>KSPROPERTY_TYPE_RELATIONS</p>
</li>
<li>
<p>KSPROPERTY_TYPE_SERIALIZESET</p>
</li>
<li>
<p>KSPROPERTY_TYPE_UNSERIALIZESET</p>
</li>
<li>
<p>KSPROPERTY_TYPE_SERIALIZERAW</p>
</li>
<li>
<p>KSPROPERTY_TYPE_UNSERIALIZERAW</p>
</li>
<li>
<p>KSPROPERTY_TYPE_SERIALIZESIZE</p>
</li>
<li>
<p>KSPROPERTY_TYPE_DEFAULTVALUES</p>
</li>
<li>
<p>KSPROPERTY_TYPE_TOPOLOGY</p>
</li>
</ul>
<p>These flags are described in <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a>.</p>
</dd>

### -field <b>InstanceSize</b>

<dd>
<p>Specifies the size in bytes of the property-instance buffer.</p>
</dd>

### -field <b>Instance</b>

<dd>
<p>Pointer to the property-instance buffer</p>
</dd>

### -field <b>ValueSize</b>

<dd>
<p>Specifies the size in bytes of the property-value buffer.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>Pointer to the property-value buffer</p>
</dd>

### -field <b>Irp</b>

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a> containing the client's original property request</p>
</dd>
</dl>

## -remarks
<p>This is the structure that the port driver passes to the miniport driver's property-handler routine. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff537722">PCPROPERTY_ITEM</a> structure contains a function pointer to a property handler that takes a <b>PCPROPERTY_REQUEST</b> pointer as its only call parameter. The port driver allocates a <b>PCPROPERTY_REQUEST</b> structure, extracts the relevant information from the original property request (which the <b>Irp</b> member points to), and loads the information into this structure before calling the handler.</p>

<p>In WDM audio, the target of a property request can be either a filter instance or a pin instance. The target can also include a node ID.</p>

<p>In the client's original property request, the property-instance data always begins with a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff537143">KSNODEPROPERTY</a> structure, but can include additional information. The port driver adjusts the <b>PCPROPERTY_REQUEST</b> structure's <b>Instance</b> member to point to this additional information, if it exists. For details, see <a href="NULL">Audio Property Handlers</a>.</p>

<p>The <b>MajorTarget</b> and <b>MinorTarget</b> members are <a href="com.iunknown">IUnknown</a> pointers to the main miniport object and an associated stream object, respectively. The property handler can query these objects for their miniport and stream interfaces. If the target for the property request is a filter instance, <b>MajorTarget</b> points to the miniport object for that filter instance, and <b>MinorTarget</b> is <b>NULL</b>. If the target is a pin instance, <b>MinorTarget</b> points to the stream object for that pin, and <b>MajorTarget</b> points to the miniport object for the filter that the pin is attached to.</p>

<p>For example, if the target for the property request is a pin instance on a WaveCyclic filter:</p>

<p>The handler can call <a href="com.iunknown_queryinterface">QueryInterface</a> on the <b>MajorTarget</b> object's <a href="com.iunknown">IUnknown</a> interface to obtain a reference to the object's <a href="https://msdn.microsoft.com/library/windows/hardware/ff536714">IMiniportWaveCyclic</a> interface.</p>

<p>The handler can call <a href="com.iunknown_queryinterface">QueryInterface</a> on the <b>MinorTarget</b> object's <a href="com.iunknown">IUnknown</a> interface to obtain a reference to the object's <a href="https://msdn.microsoft.com/library/windows/hardware/ff536715">IMiniportWaveCyclicStream</a> interface.</p>

<p>For background information about audio properties, see <a href="https://msdn.microsoft.com/ffc5834f-30c8-40b5-b57b-fe784331690c">Audio Endpoints, Properties and Events</a>. For a list of the available audio-specific properties, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536197">Audio Drivers Property Sets</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537722">PCPROPERTY_ITEM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537143">KSNODEPROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537145">KSNODEPROPERTY_AUDIO_CHANNEL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PCPROPERTY_REQUEST structure%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
