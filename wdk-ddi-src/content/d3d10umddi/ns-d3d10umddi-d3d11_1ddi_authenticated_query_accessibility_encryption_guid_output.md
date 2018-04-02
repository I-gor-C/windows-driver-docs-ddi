---
UID: NS:d3d10umddi.D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_OUTPUT
title: D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_OUTPUT
author: windows-driver-content
description: Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_CONFIGURE_ENCRYPTION_WHEN_ACCESSIBLE_GUID.
old-location: display\d3d11_1ddi_authenticated_query_accessibility_encryption_guid_output.htm
old-project: display
ms.assetid: 6b6fff46-fdc6-4b02-8176-990724121401
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_OUTPUT, D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_OUTPUT structure [Display Devices], d3d10umddi/D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_OUTPUT, display.d3d11_1ddi_authenticated_query_accessibility_encryption_guid_output
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	D3d10umddi.h
api_name:
-	D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_OUTPUT
product: Windows
targetos: Windows
req.typenames: D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_OUTPUT
---

# D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_OUTPUT structure
Contains the response to a <a href="https://msdn.microsoft.com/bb152e3d-497f-4798-86cc-6f300e24a05c">QueryAuthenticatedChannel(D3D11_1)</a> query with a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406401">D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT</a>.<b>QueryType</b> value of <b>D3D11_1DDI_AUTHENTICATED_CONFIGURE_ENCRYPTION_WHEN_ACCESSIBLE_GUID</b>.

## Syntax
```
typedef struct D3D11_1DDI_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_OUTPUT {
  D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT Output;
  UINT                                  EncryptionGuidIndex;
  GUID                                  EncryptionGuid;
};
```

## Members


`Output`

A <a href="https://msdn.microsoft.com/library/windows/hardware/hh406401">D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT</a> structure that contains a Message Authentication Code (MAC) and other data.

`EncryptionGuidIndex`

The index of the encryption GUID.

`EncryptionGuid`

A GUID that specifies a supported encryption type.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh406401">D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT</a>



<a href="https://msdn.microsoft.com/bb152e3d-497f-4798-86cc-6f300e24a05c">QueryAuthenticatedChannel(D3D11_1)</a>