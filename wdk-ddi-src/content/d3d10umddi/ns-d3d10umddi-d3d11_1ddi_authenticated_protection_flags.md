---
UID: NS:d3d10umddi.D3D11_1DDI_AUTHENTICATED_PROTECTION_FLAGS
title: D3D11_1DDI_AUTHENTICATED_PROTECTION_FLAGS
author: windows-driver-content
description: Specifies the protection level for video content.
old-location: display\d3d11_1ddi_authenticated_protection_flags.htm
old-project: display
ms.assetid: 687eb573-ea7c-4e8a-80df-65339521ec18
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: D3D11_1DDI_AUTHENTICATED_PROTECTION_FLAGS, d3d10umddi/D3D11_1DDI_AUTHENTICATED_PROTECTION_FLAGS, display.d3d11_1ddi_authenticated_protection_flags, D3D11_1DDI_AUTHENTICATED_PROTECTION_FLAGS structure [Display Devices]
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	D3d10umddi.h
apiname:
-	D3D11_1DDI_AUTHENTICATED_PROTECTION_FLAGS
product: Windows
targetos: Windows
req.typenames: D3D11_1DDI_AUTHENTICATED_PROTECTION_FLAGS
---

# D3D11_1DDI_AUTHENTICATED_PROTECTION_FLAGS structure
Specifies the protection level for video content.

## Syntax
````
typedef struct D3D11_1DDI_AUTHENTICATED_PROTECTION_FLAGS {
  union {
    struct {
      UINT ProtectionEnabled  :1;
      UINT OverlayOrFullscreenRequired  :1;
      UINT Reserved  :30;
    };
    UINT   Value;
  };
} D3D11_1DDI_AUTHENTICATED_PROTECTION_FLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |