---
UID : NC:netioddk.NPI_PROVIDER_ATTACH_CLIENT_FN
title : NPI_PROVIDER_ATTACH_CLIENT_FN
author : windows-driver-content
description : A provider module's ProviderAttachClient callback function attaches the provider module to a client module.
old-location : netvista\providerattachclient.htm
old-project : netvista
ms.assetid : 6c8e6cf1-0528-4da2-acc1-81ec9dbc23c3
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _NET_DMA_PROVIDER_CHARACTERISTICS, *PNET_DMA_PROVIDER_CHARACTERISTICS, NET_DMA_PROVIDER_CHARACTERISTICS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : netioddk.h
req.include-header : Wsk.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : PNPI_PROVIDER_ATTACH_CLIENT_FN
req.alt-loc : netioddk.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PNET_DMA_PROVIDER_CHARACTERISTICS, NET_DMA_PROVIDER_CHARACTERISTICS"
---


# NPI_PROVIDER_ATTACH_CLIENT_FN callback function
A provider module's 
  <i>ProviderAttachClient</i> callback function attaches the provider module to a client module.

## Syntax

```
NPI_PROVIDER_ATTACH_CLIENT_FN NpiProviderAttachClientFn;

NTSTATUS NpiProviderAttachClientFn(
  HANDLE NmrBindingHandle,
  PVOID ProviderContext,
  PNPI_REGISTRATION_INSTANCE ClientRegistrationInstance,
  PVOID ClientBindingContext,
  CONST VOID *ClientDispatch,
  PVOID *ProviderBindingContext,
  CONST VOID **ProviderDispatch
)
{...}
```

## Parameters

`NmrBindingHandle`

A handle used by the NMR to represent the binding between the client module and the provider
     module.

`ProviderContext`

A pointer to the provider module's registration context. The provider module passes this pointer
     to the NMR when it calls the 
     <a href="..\netioddk\nf-netioddk-nmrregisterprovider.md">NmrRegisterProvider</a> function to
     register itself with the NMR.

`ClientRegistrationInstance`

A pointer to an 
     <a href="..\netioddk\ns-netioddk-_npi_registration_instance.md">
     NPI_REGISTRATION_INSTANCE</a> structure. This structure contains the client module's registration
     data.

`ClientBindingContext`

A pointer to the client module's context for the binding between the client module and the
     provider module. The client module uses this context to keep track of the state of the binding. The
     contents of the client module's binding context are opaque to the provider module. The provider module
     passes this pointer to the client module whenever it calls any of the client module's 
     <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/network-programming-interface">NPI</a> callback functions that
     require the client module's binding context.

`*ClientDispatch`



`*ProviderBindingContext`



`**ProviderDispatch`




## Return Value

A provider module's 
     <i>ProviderAttachClient</i> callback function returns one of the following NTSTATUS codes:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The provider module successfully attached to the client module.
<dl>
<dt><b>STATUS_NOINTERFACE</b></dt>
</dl>The provider module did not attach to the client module.
<dl>
<dt><b>Other status codes</b></dt>
</dl>An error occurred.

## Remarks

The NMR calls a provider module's 
    <i>ProviderAttachClient</i> callback function whenever a client module calls the 
    <a href="..\netioddk\nf-netioddk-nmrclientattachprovider.md">NmrClientAttachProvider</a> function
    with a handle that represents a binding between the client module and the provider module.

A provider module can examine the client module's registration data. This data is in the structure
    pointed to by the 
    <i>ClientRegistrationInstance</i> parameter. The provider module uses this data to determine whether it
    will attach to the client module:

If the provider module determines that it will not attach to the client module, then the 
      <i>ProviderAttachClient</i> callback function must return STATUS_NOINTERFACE.

If the provider module attaches to the client module and it dynamically allocated memory for its
    binding context, it should free that allocated memory when the NMR calls the provider module's 
    <a href="..\netioddk\nc-netioddk-npi_provider_cleanup_binding_context_fn.md">
    ProviderCleanupBindingContext</a> callback function after the client module and provider module are
    detached from each other.

The NMR calls a provider module's 
    <i>ProviderAttachClient</i> callback function at IRQL = PASSIVE_LEVEL.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | netioddk.h (include Wsk.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\netioddk\nf-netioddk-nmrregisterprovider.md">NmrRegisterProvider</a>
</dt>
<dt>
<a href="..\netioddk\nf-netioddk-nmrclientattachprovider.md">NmrClientAttachProvider</a>
</dt>
<dt>
<a href="..\netioddk\nf-netioddk-nmrproviderdetachclientcomplete.md">
   NmrProviderDetachClientComplete</a>
</dt>
<dt>
<a href="..\netioddk\nc-netioddk-npi_provider_detach_client_fn.md">ProviderDetachClient</a>
</dt>
<dt>
<a href="..\netioddk\nc-netioddk-npi_provider_cleanup_binding_context_fn.md">
   ProviderCleanupBindingContext</a>
</dt>
<dt>
<a href="..\netioddk\ns-netioddk-_npi_registration_instance.md">NPI_REGISTRATION_INSTANCE</a>
</dt>
<dt>
<a href="..\netioddk\ns-netioddk-_npi_provider_characteristics.md">NPI_PROVIDER_CHARACTERISTICS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NPI_PROVIDER_ATTACH_CLIENT_FN callback function%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>