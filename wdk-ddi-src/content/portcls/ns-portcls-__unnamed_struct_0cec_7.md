---
UID: NS:portcls.__unnamed_struct_0cec_7
title: "*PPCPIN_DESCRIPTOR"
author: windows-driver-content
description: The PCPIN_DESCRIPTOR structure describes a pin factory.
old-location: audio\pcpin_descriptor.htm
old-project: audio
ms.assetid: 1eeee706-b7f4-4b4d-93c8-969eac7c56d9
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: PCPIN_DESCRIPTOR structure [Audio Devices], audpc-struct_475141ba-bf2e-4425-92ac-02649248e19f.xml, PPCPIN_DESCRIPTOR structure pointer [Audio Devices], *PPCPIN_DESCRIPTOR, PCPIN_DESCRIPTOR, portcls/PCPIN_DESCRIPTOR, audio.pcpin_descriptor, portcls/PPCPIN_DESCRIPTOR, PPCPIN_DESCRIPTOR
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	portcls.h
apiname:
-	PCPIN_DESCRIPTOR
product: Windows
targetos: Windows
req.typenames: "*PPCPIN_DESCRIPTOR, PCPIN_DESCRIPTOR"
---

# PCPIN_DESCRIPTOR structure
The <b>PCPIN_DESCRIPTOR</b> structure describes a pin factory.

## Syntax
````
typedef struct {
  ULONG                    MaxGlobalInstanceCount;
  ULONG                    MaxFilterInstanceCount;
  ULONG                    MinFilterInstanceCount;
  const PCAUTOMATION_TABLE *AutomationTable;
  KSPIN_DESCRIPTOR         KsPinDescriptor;
} PCPIN_DESCRIPTOR, *PPCPIN_DESCRIPTOR;
````

## Members


## Remarks
This structure is used to describe each of the pin factories that a miniport driver implements. The driver's <a href="..\portcls\ns-portcls-__unnamed_struct_0cec_9.md">PCFILTER_DESCRIPTOR</a> structure contains a pointer to an array of <b>PCPIN_DESCRIPTOR</b> structures. The number of elements in the array is equal to the number of pin factories in the filter.

The <b>MaxGlobalInstanceCount</b>, <b>MaxFilterInstanceCount</b>, and <b>MinFilterInstanceCount</b> members are maximum and minimum counts that describe the pin's resource restrictions and functional requirements. An autoinitialized <b>PCPIN_DESCRIPTOR</b> array can present only a static estimate of the available pin resources. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff536834">IPinCount::PinCount</a> method provides a means for the driver to revise its list of available pin resources dynamically as pins are allocated and freed.

The <b>MaxGlobalInstanceCount</b> value is similar in meaning to:

<ul>
<li>
The <a href="https://msdn.microsoft.com/8b7a49cc-5061-475b-ac03-cbf43954c413">PinCount</a> method's <i>GlobalPossible</i> call parameter.

</li>
<li>
The <a href="https://msdn.microsoft.com/library/windows/hardware/ff565200">KSPROPERTY_PIN_GLOBALCINSTANCES</a> property value (the KSPIN_CINSTANCES structure's <b>PossibleCount</b> member).

</li>
</ul>
The <b>MaxFilterInstanceCount</b> value is similar in meaning to:

<ul>
<li>
The <a href="https://msdn.microsoft.com/8b7a49cc-5061-475b-ac03-cbf43954c413">PinCount</a> method's <i>FilterPossible</i> call parameter.

</li>
<li>
The <a href="https://msdn.microsoft.com/library/windows/hardware/ff565193">KSPROPERTY_PIN_CINSTANCES</a> property value (the KSPIN_CINSTANCES structure's <b>PossibleCount</b> member).

</li>
</ul>
The <b>MinFilterInstanceCount</b> value is similar in meaning to:

<ul>
<li>
The <a href="https://msdn.microsoft.com/8b7a49cc-5061-475b-ac03-cbf43954c413">PinCount</a> method's <i>FilterNecessary</i> call parameter.

</li>
<li>
The <a href="https://msdn.microsoft.com/library/windows/hardware/ff565204">KSPROPERTY_PIN_NECESSARYINSTANCES</a> property value.

</li>
</ul>
When describing a bridge pin (see <a href="https://msdn.microsoft.com/823de0d5-9368-4ae6-9f11-a8daa0640edd">Audio Filter Graphs</a>), set <b>MaxGlobalInstanceCount</b>, <b>MaxFilterInstanceCount</b>, and <b>MinFilterInstanceCount</b> to zero, and set <b>AutomationTable</b> to <b>NULL</b>.

For a simple code example that shows how the <b>PCPIN_DESCRIPTOR</b> structure is used, see <a href="https://msdn.microsoft.com/bf791f40-b2fb-48fe-8350-3b926db4ead7">Exposing Filter Topology</a>.

For more information, see <a href="https://msdn.microsoft.com/1399b8e1-bd73-4052-afa5-3e992be8789b">Pin Factories</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | portcls.h (include Portcls.h) |

## See Also

<a href="..\ks\ns-ks-kspin_descriptor.md">KSPIN_DESCRIPTOR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536834">IPinCount::PinCount</a>



<a href="..\portcls\ns-portcls-__unnamed_struct_0cec_6.md">PCAUTOMATION_TABLE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff565204">KSPROPERTY_PIN_NECESSARYINSTANCES</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff565200">KSPROPERTY_PIN_GLOBALCINSTANCES</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff565193">KSPROPERTY_PIN_CINSTANCES</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PCPIN_DESCRIPTOR structure%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>