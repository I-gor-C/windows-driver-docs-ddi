---
UID : NF:sdplib.SdpFindAttributeInTree
title : SdpFindAttributeInTree function
author : windows-driver-content
description : The Bluetooth SdpFindAttributeInTree function is used to locate the specified attribute node in the tree-based representation of an SDP record.
old-location : bltooth\sdpfindattributeintree.htm
old-project : bltooth
ms.assetid : 26c71c08-3b9a-474f-a232-d7f675582d27
ms.author : windowsdriverdev
ms.date : 12/21/2017
ms.keywords : SdpFindAttributeInTree
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : sdplib.h
req.include-header : BthSdpddi.h
req.target-type : Desktop
req.target-min-winverclnt : Versions: Supported in Windows Vista, and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : SdpFindAttributeInTree
req.alt-loc : sdplib.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <= PASSIVE_LEVEL
req.typenames : "*PSDCMD_DESCRIPTOR, SDCMD_DESCRIPTOR"
req.product : Windows 10 or later.
---


# SdpFindAttributeInTree function
The Bluetooth 
  <b>SdpFindAttributeInTree</b> function is used to locate the specified attribute node in the tree-based
  representation of an SDP record.

## Syntax

````
NTSTATUS SdpFindAttributeInTree(
  _In_  PSDP_TREE_ROOT_NODE Tree,
  _In_  USHORT              AttribId,
  _Out_ PSDP_NODE           *AttribValue
);
````

## Parameters

`Tree`

The root node of the tree-based representation of the SDP record to search.

`AttribId`

The identifier of the attribute node to locate.

`Attribute`




## Return Value

Possible return values include:

## Remarks

The 
    <b>SdpFindAttributeInTree</b> function returns the address of the requested node in the tree; it does not
    perform a copy. This node pointer is valid until the SDP tree that it references is freed.

Bluetooth profile drivers can obtain a pointer to this function through the 
    <a href="..\bthsdpddi\ns-bthsdpddi-_bthddi_sdp_parse_interface.md">
    BTHDDI_SDP_PARSE_INTERFACE</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | sdplib.h (include BthSdpddi.h) |
| **Library** |  |
| **IRQL** | <= PASSIVE_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\bthsdpddi\ns-bthsdpddi-_bthddi_sdp_parse_interface.md">BTHDDI_SDP_PARSE_INTERFACE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20SdpFindAttributeInTree function%20 RELEASE:%20(12/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>