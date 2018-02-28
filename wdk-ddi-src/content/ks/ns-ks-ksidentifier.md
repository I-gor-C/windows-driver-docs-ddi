---
UID: NS:ks.KSIDENTIFIER
title: KSIDENTIFIER
author: windows-driver-content
description: The KSIDENTIFIER structure specifies a GUID that uniquely identifies a related set of GUIDs, and an index value to refer to a specific member within that set.
old-location: stream\ksidentifier.htm
old-project: stream
ms.assetid: b89977da-d3ac-4f1f-867e-b3b7912b955d
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PKSDEGRADE, *PKSEVENT, *PKSIDENTIFIER, *PKSMETHOD, *PKSPIN_INTERFACE, *PKSPIN_MEDIUM, *PKSPROPERTY, KSDEGRADE, KSEVENT, KSIDENTIFIER, KSIDENTIFIER structure [Streaming Media Devices], KSMETHOD, KSPIN_INTERFACE, KSPIN_MEDIUM, KSPROPERTY, PKSIDENTIFIER, PKSIDENTIFIER structure pointer [Streaming Media Devices], ks-struct_652a0465-0c2b-4e46-ac43-7a6c5bbdaf80.xml, ks/KSIDENTIFIER, ks/PKSIDENTIFIER, stream.ksidentifier"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ks.h
api_name:
-	KSIDENTIFIER
product: Windows
targetos: Windows
req.typenames: KSIDENTIFIER, *PKSIDENTIFIER
---

# KSIDENTIFIER structure
The KSIDENTIFIER structure specifies a GUID that uniquely identifies a related set of GUIDs, and an index value to refer to a specific member within that set.

## Syntax
````
typedef struct {
  union {
    GUID     Set;
    ULONG    Id;
    ULONG    Flags;
    LONGLONG Alignment;
  };
} KSIDENTIFIER, *PKSIDENTIFIER;
````

## Members


## Remarks
The <a href="https://msdn.microsoft.com/library/windows/hardware/ff561744">KSEVENT</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff563398">KSMETHOD</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> structures are aliases for the KSIDENTIFIER structure. As such, their definitions are identical. 

The use of an ID within the set allows one to perform a single large compare for a set identifier, then smaller quick compares (for example, by using a switch statement for identifiers within a set). For example, a <i>property set</i> is referred to by a unique GUID identifier, and properties within that set are referred to by the short ID.

<i>Method</i>, <i>Event</i>, <i>Interface</i>, and <i>medium sets</i> can be thought of as "classes" of sets.

The size of the output buffer passed determines what data is returned from a KSPROPERTY_TYPE_BASICSUPPORT request. If the output buffer is the size of a ULONG, only the access flags are returned. If the output buffer is the size of the <a href="..\ks\ns-ks-ksproperty_description.md">KSPROPERTY_DESCRIPTION</a> structure, the structure is filled with the access flags, the inclusive size of the entire values information, the property value type information, and the number of member lists that correspond to the structure.

For a KSPROPERTY_TYPE_RELATIONS request, data returned also depends on the size of the output buffer. If the output buffer size is zero, the size required to return the related properties is returned in <b>BytesReturned</b> with a warning status of STATUS_BUFFER_OVERFLOW. If the buffer is the size of a <a href="..\ks\ns-ks-ksmultiple_item.md">KSMULTIPLE_ITEM</a> structure, both the byte size and count of relations is returned. Otherwise, the buffer is expected to be long enough to return the KSMULTIPLE_ITEM structure and all related property identifiers, which is returned as a list of <b>KSIDENTIFIER</b> structures.

KSPROPERTY_TYPE_SERIALIZESET and KSPROPERTY_TYPE_UNSERIALIZESET requests allow interaction with multiple properties with a single call from the client. If the kernel streaming handler is being used to process property requests, these are broken up into multiple calls by the <a href="..\ks\nf-ks-kspropertyhandler.md">KsPropertyHandler</a> function. When using this handler, the property set definition controls which properties are to be serialized. 

For serialization requests, the <b>SerializedSize</b> member of the relevant <a href="..\ks\ns-ks-ksproperty_item.md">KSPROPERTY_ITEM</a> structure is checked for a nonzero value that indicates the size, in bytes, of the property. If the value of the SerializedSize member is 1, it is unknown and must be queried (all unknown properties begin with a KSMULTIPLE_ITEM structure that can be queried separately). To query for the total size a serialization would take, the client passes a zero length buffer in the call to <b>DeviceIoControl</b>. <b>BytesReturned</b> then returns the size, in bytes, that the buffer must be to serialize the set, and a warning status of STATUS_BUFFER_OVERFLOW. A buffer allocated that size can then be filled with the serialized data.

The format of the serialization buffer is a <a href="..\ks\ns-ks-ksproperty_serialhdr.md">KSPROPERTY_SERIALHDR</a>, followed by serialized properties. Each property that follows contains a header (<a href="..\ks\ns-ks-ksproperty_serial.md">KSPROPERTY_SERIAL</a>), followed by the property data, with the start of each property on FILE_LONG_ALIGNMENT. Note that the serial header structure is defined to be on FILE_LONG_ALIGNMENT.

KSPROPERTY_TYPE_SERIALIZERAW and KSPROPERTY_TYPE_UNSERIALIZERAW are supported if a property item handler exists. The <b>KsPropertyHandler</b> function invokes the handler provided by the minidriver. The buffer size required for serialization can also be queried by passing a zero-length buffer to a serialize raw request. Because handlers are attached to property items rather than the property set, a specific item within the property set must be specified in the <b>Property</b> parameter. This handler may deal with multiple properties within the set.

The <a href="https://msdn.microsoft.com/library/windows/hardware/ff561744">KSEVENT</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff563398">KSMETHOD</a>, and KSPROPERTY structures are aliases for the KSIDENTIFIER structure. As such, their definitions are identical.

Microsoft provides several system-defined property set GUIDs. Minidrivers specify one of these GUIDs in the <b>Set</b> member. Kernel streaming property sets typically begin with either a <i>KSPROPSETID</i> or a <i>PROPSETID</i> prefix. Kernel streaming property sets are defined in <i>ks.h</i>, <i>ksmedia.h</i>, <i>bdamedia.h</i>, and possibly other header files.

For more information about kernel streaming properties, see <a href="https://msdn.microsoft.com/933bbe81-92d8-4bcc-b935-9ae929464ca1">KS Properties, Events, and Methods</a>.

Microsoft provides several system-defined event set GUIDs. Minidrivers specify one of these GUIDs in the <b>Set</b> member. Kernel streaming event sets typically begin with a <i>KSEVENTSETID</i> prefix. Kernel streaming event sets are defined in <i>ks.h</i>, <i>ksmedia.h</i>, <i>bdamedia.h</i>, and possibly other header files.

For more information about kernel streaming events, see <a href="https://msdn.microsoft.com/933bbe81-92d8-4bcc-b935-9ae929464ca1">KS Properties, Events, and Methods</a>.

Microsoft provides several system-defined method set GUIDs. Minidrivers specify one of these GUIDs in the <b>Set</b> member. Kernel streaming method sets typically begin with a <i>KSMETHODSETID</i> prefix. Kernel streaming method sets are defined in <i>ks.h</i>, <i>ksmedia.h</i>, <i>bdamedia.h</i>, and possibly other header files.

For more information about kernel streaming methods, see <a href="https://msdn.microsoft.com/933bbe81-92d8-4bcc-b935-9ae929464ca1">KS Properties, Events, and Methods</a>.

A client can use the IOCTL_KS_METHOD request along with the KSMETHOD structure to execute methods on a kernel streaming object that the minidriver handles. For more information, see <a href="https://msdn.microsoft.com/1d7bd6f4-0aaf-4d77-8132-f551fd2ecbd2">KS Methods</a>.

The KSPIN_MEDIUM structure identifies a medium, with a unique medium GUID and instance identifier, which is generated in a bus-specific manner. There is a reserved identifier value KSMEDIUM_TYPE_ANYINSTANCE that is used when bus instances are not of concern. For example, the KSMEDIUMSETID_Standard refers to the system bus, of which there should only be one. So this instance identifier is always used just as a convenience.

A pin may support multiple mediums and interfaces on those mediums. The way in which a pin is described implies that the list of interfaces is supported on all mediums enumerated for a pin. If there is a case in which this is not true, another pin may be used to describe each subset of interfaces for the specific mediums.

The medium is also cached by kernel streaming to speed up the search for a possible connection.

An example of use of this structure can be found in a tuner sample, in which KSPIN_MEDIUM represents unique connections between tuners, crossbars, and other tuner components.

The <a href="https://msdn.microsoft.com/library/windows/hardware/ff561744">KSEVENT</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff563398">KSMETHOD</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> and KSDEGRADE structures are aliases for the <b>KSIDENTIFIER</b> structure. As such, their definitions are identical.

The <b>Flags</b> member can contain different values based on the type of signal degradation that the client employs. See <a href="https://msdn.microsoft.com/359e6e12-903f-4037-8f35-b090ce41f770">Quality Management</a>. for more details on different strategies for solving QM problems by reducing signal quality.

Because <b>Flags</b> contains a ULONG value, multiple Skip requests may be needed to remedy the QM issue.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff563398">KSMETHOD</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561744">KSEVENT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSIDENTIFIER structure%20 RELEASE:%20(2/23/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>