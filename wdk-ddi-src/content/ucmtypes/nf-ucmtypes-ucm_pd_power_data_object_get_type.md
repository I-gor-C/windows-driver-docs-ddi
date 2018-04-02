---
UID: NF:ucmtypes.UCM_PD_POWER_DATA_OBJECT_GET_TYPE
title: UCM_PD_POWER_DATA_OBJECT_GET_TYPE function
author: windows-driver-content
description: Retrieves the type of Power Data Object from the UCM_PD_POWER_DATA_OBJECT structure.
old-location: buses\ucm_pd_power_data_object_get_type.htm
old-project: usbref
ms.assetid: ACB0AB92-5EC8-4792-AB40-853FC5AAD125
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: UCM_PD_POWER_DATA_OBJECT_GET_TYPE, UCM_PD_POWER_DATA_OBJECT_GET_TYPE function [Buses], buses.ucm_pd_power_data_object_get_type, ucmtypes/UCM_PD_POWER_DATA_OBJECT_GET_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucmtypes.h
req.include-header: Ucmcx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 2.15
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
-	Ucmtypes.h
api_name:
-	UCM_PD_POWER_DATA_OBJECT_GET_TYPE
product:
- Windows
targetos: Windows
req.typenames: UCM_TYPEC_PARTNER
req.product: Windows 10 or later.
---


# UCM_PD_POWER_DATA_OBJECT_GET_TYPE function
Retrieves the type of Power Data Object from the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187935">UCM_PD_POWER_DATA_OBJECT</a> structure.

## Syntax

```
UCM_PD_POWER_DATA_OBJECT_TYPE UCM_PD_POWER_DATA_OBJECT_GET_TYPE(
  PUCM_PD_POWER_DATA_OBJECT Pdo
);
```

## Parameters

`Pdo`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/mt187935">UCM_PD_POWER_DATA_OBJECT</a> structure that contains the type of Power Data Object.


## Return Value

Returns the <b>Common.Type</b> member of the  <a href="https://msdn.microsoft.com/library/windows/hardware/mt187935">UCM_PD_POWER_DATA_OBJECT</a> structure.

## Remarks

For information about the Power Data Object including the types of object, see Power Delivery specification. The Type member of <a href="https://msdn.microsoft.com/library/windows/hardware/mt187935">UCM_PD_POWER_DATA_OBJECT</a> indicates the type of Power Data Object.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.15 |
| **Minimum UMDF version** | 2.15 |
| **Header** | ucmtypes.h (include Ucmcx.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt187935">UCM_PD_POWER_DATA_OBJECT</a>