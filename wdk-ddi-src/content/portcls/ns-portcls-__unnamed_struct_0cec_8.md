---
UID: NS:portcls.__unnamed_struct_0cec_8
title: "*PPCNODE_DESCRIPTOR"
author: windows-driver-content
description: The PCNODE_DESCRIPTOR structure describes a node in the filter that a topology miniport driver implements.
old-location: audio\pcnode_descriptor.htm
old-project: audio
ms.assetid: e83051ca-07fa-439d-8b0f-cbe6d84679a7
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: audio.pcnode_descriptor, PCNODE_DESCRIPTOR structure [Audio Devices], portcls/PPCNODE_DESCRIPTOR, audpc-struct_275973f3-8db9-4b2c-ad30-e375b5e69656.xml, PCNODE_DESCRIPTOR, *PPCNODE_DESCRIPTOR, PPCNODE_DESCRIPTOR structure pointer [Audio Devices], PPCNODE_DESCRIPTOR, portcls/PCNODE_DESCRIPTOR
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
-	PCNODE_DESCRIPTOR
product: Windows
targetos: Windows
req.typenames: "*PPCNODE_DESCRIPTOR, PCNODE_DESCRIPTOR"
---

# *PPCNODE_DESCRIPTOR structure
The <b>PCNODE_DESCRIPTOR</b> structure describes a node in the filter that a topology miniport driver implements.

## Syntax
````
typedef struct {
  ULONG                    Flags;
  const PCAUTOMATION_TABLE *AutomationTable;
  const GUID               *Type;
  const GUID               *Name;
} PCNODE_DESCRIPTOR, *PPCNODE_DESCRIPTOR;
````

## Members


## Remarks
If a filter contains only a single node of the type specified by the <b>Type</b> member, then the <b>Name</b> member can be specified as <b>NULL</b> because the <b>Type</b> value is sufficient to uniquely identify the node within the filter. If the filter contains two or more nodes of the same type, the <b>Name</b> members for those nodes must be non-<b>NULL</b>.

For example, if a filter contains a single SUM node, the <b>Type</b> member for that node points to GUID value <a href="https://msdn.microsoft.com/library/windows/hardware/ff537196">KSNODETYPE_SUM</a>, and the <b>Name</b> member is set to <b>NULL</b>. When queried for the name of that node, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565809">KSPROPERTY_TOPOLOGY_NAME</a> property, after determining that the node's <b>Name</b> value is <b>NULL</b>, retrieves the name string from the registry entry for the KSNODETYPE_SUM GUID. However, the same filter might contain several volume nodes, in which case the <b>Type</b> values for these nodes all point to the same GUID value, <a href="https://msdn.microsoft.com/library/windows/hardware/ff537208">KSNODETYPE_VOLUME</a>, and the <b>Name</b> value must uniquely identify each of the volume nodes. The <b>Name</b> value for the wave-input volume control node, for example, should point to GUID value KSAUDFNAME_WAVE_IN_VOLUME (defined in ksmedia.h). The registry entry for this GUID contains the name string that the KSPROPERTY_TOPOLOGY_NAME property retrieves for the node.

The <a href="..\portcls\ns-portcls-__unnamed_struct_0cec_9.md">PCFILTER_DESCRIPTOR</a> structure contains a pointer to an array of <b>PCNODE_DESCRIPTOR</b> structures.

For a simple code example that shows how the <b>PCNODE_DESCRIPTOR</b> structure is used, see <a href="https://msdn.microsoft.com/bf791f40-b2fb-48fe-8350-3b926db4ead7">Exposing Filter Topology</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | portcls.h (include Portcls.h) |

## See Also

<a href="..\portcls\ns-portcls-__unnamed_struct_0cec_6.md">PCAUTOMATION_TABLE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff565809">KSPROPERTY_TOPOLOGY_NAME</a>



<a href="..\portcls\ns-portcls-__unnamed_struct_0cec_9.md">PCFILTER_DESCRIPTOR</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PCNODE_DESCRIPTOR structure%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>