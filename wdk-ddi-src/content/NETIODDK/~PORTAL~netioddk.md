# Declarations in the netioddk header
This header Netioddk contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [NmrWaitForProviderDeregisterComplete function](nf-netioddk-nmrwaitforproviderderegistercomplete.md) | The NmrWaitForProviderDeregisterComplete function waits for the deregistration of a provider module to complete. |
| [NmrClientDetachProviderComplete function](nf-netioddk-nmrclientdetachprovidercomplete.md) | The NmrClientDetachProviderComplete function notifies the NMR that a client module has completed detaching from a provider module. |
| [NmrDeregisterClient function](nf-netioddk-nmrderegisterclient.md) | The NmrDeregisterClient function deregisters a client module from the NMR. |
| [NmrRegisterClient function](nf-netioddk-nmrregisterclient.md) | The NmrRegisterClient function registers a client module with the NMR. |
| [NmrProviderDetachClientComplete function](nf-netioddk-nmrproviderdetachclientcomplete.md) | The NmrProviderDetachClientComplete function notifies the NMR that a provider module has completed detaching from a client module. |
| [NmrDeregisterProvider function](nf-netioddk-nmrderegisterprovider.md) | The NmrDeregisterProvider function deregisters a provider module from the NMR. |
| [NmrClientAttachProvider function](nf-netioddk-nmrclientattachprovider.md) | The NmrClientAttachProvider function attaches a client module to a provider module. |
| [NmrWaitForClientDeregisterComplete function](nf-netioddk-nmrwaitforclientderegistercomplete.md) | The NmrWaitForClientDeregisterComplete function waits for the deregistration of a client module to complete. |
| [NmrRegisterProvider function](nf-netioddk-nmrregisterprovider.md) | The NmrRegisterProvider function registers a provider module with the NMR. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [NPI structure](ns-netioddk--npi.md) | TBD |
| [NPI_CLIENT_CHARACTERISTICS structure](ns-netioddk--npi-client-characteristics.md) | TBD |
| [NPI_REGISTRATION_INSTANCE structure](ns-netioddk--npi-registration-instance.md) | TBD |
| [NPI_PROVIDER_CHARACTERISTICS structure](ns-netioddk--npi-provider-characteristics~r1.md) | The NPI_PROVIDER_CHARACTERISTICS structure defines the characteristics of a provider module. |
| [NPI_CLIENT_CHARACTERISTICS structure](ns-netioddk--npi-client-characteristics~r1.md) | The NPI_CLIENT_CHARACTERISTICS structure defines the characteristics of a client module. |
| [NPI_REGISTRATION_INSTANCE structure](ns-netioddk--npi-registration-instance~r1.md) | The NPI_REGISTRATION_INSTANCE structure defines the data related to the registration of a network module with the NMR. |
| [NPI_PROVIDER_CHARACTERISTICS structure](ns-netioddk--npi-provider-characteristics.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [NPI_PROVIDER_ATTACH_CLIENT_FN callback function](nc-netioddk-npi-provider-attach-client-fn.md) | TBD |
| [NPI_CLIENT_CLEANUP_BINDING_CONTEXT_FN callback function](nc-netioddk-npi-client-cleanup-binding-context-fn.md) | TBD |
| [NPI_CLIENT_ATTACH_PROVIDER_FN callback function](nc-netioddk-npi-client-attach-provider-fn.md) | TBD |
| [NPI_CLIENT_DETACH_PROVIDER_FN callback function](nc-netioddk-npi-client-detach-provider-fn.md) | TBD |
| [NPI_PROVIDER_CLEANUP_BINDING_CONTEXT_FN callback function](nc-netioddk-npi-provider-cleanup-binding-context-fn.md) | TBD |
| [NPI_PROVIDER_DETACH_CLIENT_FN callback function](nc-netioddk-npi-provider-detach-client-fn.md) | TBD |

This header is used in these topics:

- [netvista](..content/_netvista)
