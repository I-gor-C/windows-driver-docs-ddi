---
UID: NE:ks.KSPROPERTY_CONNECTION
title: KSPROPERTY_CONNECTION
author: windows-driver-content
description: "."
old-location: stream\ksproperty_connection.htm
old-project: stream
ms.assetid: 5129FB6F-528B-4795-9798-9707DCD57A7D
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KSPROPERTY_CONNECTION, KSPROPERTY_CONNECTION enumeration [Streaming Media Devices], KSPROPERTY_CONNECTION_ACQUIREORDERING, KSPROPERTY_CONNECTION_ALLOCATORFRAMING, KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX, KSPROPERTY_CONNECTION_DATAFORMAT, KSPROPERTY_CONNECTION_PRIORITY, KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT, KSPROPERTY_CONNECTION_STARTAT, KSPROPERTY_CONNECTION_STATE, ks/KSPROPERTY_CONNECTION, ks/KSPROPERTY_CONNECTION_ACQUIREORDERING, ks/KSPROPERTY_CONNECTION_ALLOCATORFRAMING, ks/KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX, ks/KSPROPERTY_CONNECTION_DATAFORMAT, ks/KSPROPERTY_CONNECTION_PRIORITY, ks/KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT, ks/KSPROPERTY_CONNECTION_STARTAT, ks/KSPROPERTY_CONNECTION_STATE, stream.ksproperty_connection
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ks.h
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
-	Ks.h
api_name:
-	KSPROPERTY_CONNECTION
product: Windows
targetos: Windows
req.typenames: KSPROPERTY_CONNECTION
---

# KSPROPERTY_CONNECTION Enumeration


## Syntax
````
typedef enum  { 
  KSPROPERTY_CONNECTION_STATE,
  KSPROPERTY_CONNECTION_PRIORITY,
  KSPROPERTY_CONNECTION_DATAFORMAT,
  KSPROPERTY_CONNECTION_ALLOCATORFRAMING,
  KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT,
  KSPROPERTY_CONNECTION_ACQUIREORDERING,
  KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX,
  KSPROPERTY_CONNECTION_STARTAT
} KSPROPERTY_CONNECTION;
````

## Constants

<table>
            
                <tr>
                    <td>KSPROPERTY_CONNECTION_STATE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>KSPROPERTY_CONNECTION_PRIORITY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>KSPROPERTY_CONNECTION_DATAFORMAT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>KSPROPERTY_CONNECTION_ALLOCATORFRAMING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>KSPROPERTY_CONNECTION_ACQUIREORDERING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>KSPROPERTY_CONNECTION_STARTAT</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ks.h |