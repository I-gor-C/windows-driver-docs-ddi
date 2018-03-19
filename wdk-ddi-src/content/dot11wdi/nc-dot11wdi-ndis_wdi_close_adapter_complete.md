---
UID: NC:dot11wdi.NDIS_WDI_CLOSE_ADAPTER_COMPLETE
title: NDIS_WDI_CLOSE_ADAPTER_COMPLETE
author: windows-driver-content
description: The NdisWdiCloseAdapterComplete callback function is called by the IHV when a Close Task operation from MiniportWdiCloseAdapter has been successfully started.
old-location: netvista\ndiswdicloseadaptercomplete.htm
old-project: netvista
ms.assetid: 42500F6F-8E97-454F-819F-8EA3785C0D04
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: NDIS_WDI_CLOSE_ADAPTER_COMPLETE, NdisWdiCloseAdapterComplete, NdisWdiCloseAdapterComplete callback function [Network Drivers Starting with Windows Vista], dot11wdi/NdisWdiCloseAdapterComplete, netvista.ndiswdicloseadaptercomplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	UserDefined
api_location:
-	dot11wdi.h
api_name:
-	NdisWdiCloseAdapterComplete
product: Windows
targetos: Windows
req.typenames: SYNTH_STATS, *PSYNTH_STATS
---


# NDIS_WDI_CLOSE_ADAPTER_COMPLETE callback function
The NdisWdiCloseAdapterComplete callback function is called by the IHV when a Close Task operation from <a href="..\dot11wdi\nc-dot11wdi-miniport_wdi_close_adapter.md">MiniportWdiCloseAdapter</a> has been successfully started.

This is a control path callback inside <a href="..\dot11wdi\ns-dot11wdi-_ndis_wdi_init_parameters.md">NDIS_WDI_INIT_PARAMETERS</a>.

## Syntax

```
NDIS_WDI_CLOSE_ADAPTER_COMPLETE NdisWdiCloseAdapterComplete;

void NdisWdiCloseAdapterComplete(
  NDIS_HANDLE MiniportAdapterHandle,
  NDIS_STATUS CompletionStatus
)
{...}
```

## Parameters

`MiniportAdapterHandle`

The miniport handle.

`CompletionStatus`

The completion status.


## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | dot11wdi.h |

## See Also

<a href="..\dot11wdi\nc-dot11wdi-miniport_wdi_close_adapter.md">MiniportWdiCloseAdapter</a>



<a href="..\dot11wdi\ns-dot11wdi-_ndis_wdi_init_parameters.md">NDIS_WDI_INIT_PARAMETERS</a>