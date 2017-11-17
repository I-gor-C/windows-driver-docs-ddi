---
UID: NC.dispmprt.DXGKDDI_NOTIFY_ACPI_EVENT
title: DXGKDDI_NOTIFY_ACPI_EVENT
author: windows-driver-content
description: 
ms.assetid: 34938890-e72c-4b27-b636-6c7e84e3f3e6
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dispmprt.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# DXGKDDI_NOTIFY_ACPI_EVENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_NOTIFY_ACPI_EVENT DxgkddiNotifyAcpiEvent; 

// Definition

NTSTATUS DxgkddiNotifyAcpiEvent 
(
	IN_CONST_PVOID MiniportDeviceContext
	IN_DXGK_EVENT_TYPE EventType
	IN_ULONG Event
	IN_PVOID Argument
	OUT_PULONG AcpiFlags
)
{...}

DXGKDDI_NOTIFY_ACPI_EVENT PDXGKDDI_NOTIFY_ACPI_EVENT


```

## -parameters

### -param MiniportDeviceContext: 
### -param EventType: 
### -param Event: 
### -param Argument: 
### -param AcpiFlags: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also