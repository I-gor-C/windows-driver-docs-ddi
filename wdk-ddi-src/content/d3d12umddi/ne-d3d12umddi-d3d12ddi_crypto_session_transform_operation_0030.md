---
UID: NE:d3d12umddi.D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030
title: D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030
author: windows-driver-content
description: The crypto session transform operations.
old-location: display\d3d12ddi-crypto-session-transform-operation-0030.htm
old-project: display
ms.assetid: 20d49b34-436a-4bc3-9b32-25f03478c90a
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030, D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030 enumeration [Display Devices], D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT, D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT_HEADER, D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT_WITH_HEADER, D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_NONE, D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_TRANSCRYPT, D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_TRANSCRYPT_WITH_HEADER, d3d12umddi/D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030, d3d12umddi/D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT, d3d12umddi/D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT_HEADER, d3d12umddi/D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT_WITH_HEADER, d3d12umddi/D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_NONE, d3d12umddi/D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_TRANSCRYPT, d3d12umddi/D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_TRANSCRYPT_WITH_HEADER, display.d3d12ddi-crypto-session-transform-operation-0030
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d12umddi.h
req.include-header: 
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
-	d3d12umddi.h
api_name:
-	D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030
product: Windows
targetos: Windows
req.typenames: D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030
---

# D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030 Enumeration
The crypto session transform operations.

## Syntax
````
typedef enum _D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030 { 
  D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_NONE,
  D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT,
  D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT_WITH_HEADER,
  D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_TRANSCRYPT,
  D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_TRANSCRYPT_WITH_HEADER,
  D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT_HEADER
} D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030;
````

## Constants

<table>
            
                <tr>
                    <td>D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT</td>
                    <td>The crypto session transform operation is decrypt.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT_HEADER</td>
                    <td>The crypto session transform operation is decrypt header.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_DECRYPT_WITH_HEADER</td>
                    <td>The crypto session transform operation is decrypt with header.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_NONE</td>
                    <td>The crypto session transform operation type is not available.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_TRANSCRYPT</td>
                    <td>The crypto session transform operation is transcrypt.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030_TRANSCRYPT_WITH_HEADER</td>
                    <td>The crypto session transform operation is transcrypt with header.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h |