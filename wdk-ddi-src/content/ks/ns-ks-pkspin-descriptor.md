---
UID: NS.ks.PKSPIN_DESCRIPTOR
title: PKSPIN_DESCRIPTOR
author: windows-driver-content
description: The KSPIN_DESCRIPTOR structure describes the basic KSPROPSETID_Pin properties of a pin type.
old-location: stream\kspin_descriptor.htm
old-project: stream
ms.assetid: 0e7fccd1-1ced-41e7-8e75-8f4fa496ea06
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSPIN_DESCRIPTOR, KSPIN_DESCRIPTOR, *PKSPIN_DESCRIPTOR
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
req.alt-api: KSPIN_DESCRIPTOR
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

# PKSPIN_DESCRIPTOR structure



## -description
<p>The KSPIN_DESCRIPTOR structure describes the basic <a href="https://msdn.microsoft.com/library/windows/hardware/ff566584">KSPROPSETID_Pin</a> properties of a pin type.</p>


## -syntax

````
typedef struct {
  ULONG                 InterfacesCount;
  const KSPIN_INTERFACE *Interfaces;
  ULONG                 MediumsCount;
  const KSPIN_MEDIUM    *Mediums;
  ULONG                 DataRangesCount;
  const PKSDATARANGE    *DataRanges;
  KSPIN_DATAFLOW        DataFlow;
  KSPIN_COMMUNICATION   Communication;
  const GUID            *Category;
  const GUID            *Name;
  union {
    LONGLONG Reserved;
    struct {
      ULONG        ConstrainedDataRangesCount;
      PKSDATARANGE *ConstrainedDataRanges;
    };
  };
} KSPIN_DESCRIPTOR, *PKSPIN_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>InterfacesCount</b>

<dd>
<p>Specifies the size of the array pointed to by <b>Interfaces</b>.</p>
</dd>

### -field <b>Interfaces</b>

<dd>
<p>An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563537">KSPIN_INTERFACE</a> structures specifying the interfaces supported by this pin type.</p>
</dd>

### -field <b>MediumsCount</b>

<dd>
<p>Specifies the number of elements in the array pointed to by <b>Mediums</b>.</p>
</dd>

### -field <b>Mediums</b>

<dd>
<p>An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563538">KSPIN_MEDIUM</a> structures specifying the mediums supported by this pin type.</p>
</dd>

### -field <b>DataRangesCount</b>

<dd>
<p>Specifies the size of the array pointed to by <b>DataRanges</b>.</p>
</dd>

### -field <b>DataRanges</b>

<dd>
<p>An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a> structures specifying the data ranges supported by this pin type.</p>
</dd>

### -field <b>DataFlow</b>

<dd>
<p>Specifies either <b>KSPIN_DATAFLOW_IN</b> or KSPIN_DATAFLOW_OUT. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff565197">KSPROPERTY_PIN_DATAFLOW</a>.</p>
</dd>

### -field <b>Communication</b>

<dd>
<p>Specifies KSPIN_COMMUNICATION_NONE, KSPIN_COMMUNICATION_SINK, KSPIN_COMMUNICATION_SOURCE, KSPIN_COMMUNICATION_BOTH or KSPIN_COMMUNICATION_BRIDGE. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff565194">KSPROPERTY_PIN_COMMUNICATION</a> for the meaning of each value.</p>
</dd>

### -field <b>Category</b>

<dd>
<p>Specifies a pointer to a KS pin category GUID. The KS pin category GUID identifies the general category of functionality that the pin provides. Examples of KS pin category GUIDs are KSNODETYPE_SPEAKER, KSNODETYPE_HEADPHONES, and KSNODETYPE_MICROPHONE, which are all defined in <i>Ksmedia.h</i>. Also see <a href="NULL">Pin Category Property</a>.</p>
</dd>

### -field <b>Name</b>

<dd>
<p>Specifies the GUID of the localized Unicode string name for the pin type, stored in the Registry.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Not used.  A member of an unnamed union used to force proper alignment on the unnamed structure.</p>
</dd>

### -field <b>ConstrainedDataRangesCount</b>

<dd>
<p>Specifies the number of entries in the array pointed to by <b>ConstrainedDataRanges</b>.</p>
</dd>

### -field <b>ConstrainedDataRanges</b>

<dd>
<p>Points to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a> structures. Indicates the set of data ranges the pin type currently supports, based on the driver's internal state.</p>
</dd>
</dl>

## -remarks
<p>Drivers typically define one KSPIN_DESCRIPTOR structure for each pin type they support.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566584">KSPROPSETID_Pin</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563538">KSPIN_MEDIUM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565197">KSPROPERTY_PIN_DATAFLOW</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565194">KSPROPERTY_PIN_COMMUNICATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPIN_DESCRIPTOR structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
