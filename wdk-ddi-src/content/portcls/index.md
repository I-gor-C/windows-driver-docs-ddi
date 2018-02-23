---
UID: NA:portcls
ms.assetid: 6e1a2bb6-6b07-3266-83bb-aa08030d97d6
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# portcls.h header



portcls.h contains the following programming interfaces:



## Interfaces
| Title | Description |
| ---- |:---- |
| [IAdapterPnpManagement](nn-portcls-iadapterpnpmanagement.md) | IAdapterPnpManagement is an interface that adapters should implement and register if they want to receive PnP management messages. |
| [IAdapterPowerManagement](nn-portcls-iadapterpowermanagement.md) | The IAdapterPowerManagement interface is used to manage the power state of an audio adapter. |
| [IAdapterPowerManagement2](nn-portcls-iadapterpowermanagement2.md) | The IAdapterPowerManagement2 interface inherits from IUnknown and it is used to manage the power state of an audio adapter. |
| [IAdapterPowerManagement3](nn-portcls-iadapterpowermanagement3.md) | The IAdapterPowerManagement3 interface inherits from IUnknown, and it is used for receiving power management messages. |
| [IDmaChannel](nn-portcls-idmachannel.md) | The IDmaChannel interface provides an abstraction of a DMA channel and its associated DMA buffer and usage parameters. |
| [IDmaChannelSlave](nn-portcls-idmachannelslave.md) | The IDmaChannelSlave interface provides methods for monitoring and controlling a DMA channel for a subordinate device (as described in Introduction to Adapter Objects). |
| [IDrmPort](nn-portcls-idrmport.md) | The IDrmPort interface is used by a WaveCyclic or WavePci miniport driver to manage DRM-protected content (see Digital Rights Management). |
| [IDrmPort2](nn-portcls-idrmport2.md) | The IDrmPort2 interface is used by a WaveCyclic or WavePci miniport driver to manage DRM-protected content (see Digital Rights Management). |
| [IInterruptSync](nn-portcls-iinterruptsync.md) | The IInterruptSync interface represents an interrupt sync object that synchronizes the execution of a list of interrupt service routines (ISRs) with non-ISR routines. |
| [IMiniport](nn-portcls-iminiport.md) | The IMiniport interface is the generic miniport interface that all miniport objects support. IMiniport inherits from the IUnknown interface. |
| [IMiniportAudioEngineNode](nn-portcls-iminiportaudioenginenode.md) | This interface allows a miniport driver to use KS properties that access the audio engine via a KS filter handle. |
| [IMiniportAudioSignalProcessing](nn-portcls-iminiportaudiosignalprocessing.md) | The IMiniportAudioSignalProcessing interface is implemented by the WaveRT miniport component of any audio driver, if any of its pins support audio signal processing modes. |
| [IMiniportMidi](nn-portcls-iminiportmidi.md) | The IMiniportMidi interface is the primary interface for a MIDI miniport driver for a MIDI synthesizer device. |
| [IMiniportMidiStream](nn-portcls-iminiportmidistream.md) | The IMiniportMidiStream interface represents the MIDI stream that flows through a pin on a MIDI filter. |
| [IMiniportPnpNotify](nn-portcls-iminiportpnpnotify.md) | IMiniportPnpNotify is an optional interface to allow miniport objects (audio subdevices) to receive PnP state change notifications. |
| [IMiniportStreamAudioEngineNode](nn-portcls-iminiportstreamaudioenginenode.md) | This interface allows a miniport driver to use KS properties that access the audio engine via a pin instance handle. |
| [IMiniportStreamAudioEngineNode2](nn-portcls-iminiportstreamaudioenginenode2.md) | The IMiniportStreamAudioEngineNode2 interface allows an audio miniport driver to extend the capabilities of the IMiniportStreamAudioEngineNode interface. |
| [IMiniportTopology](nn-portcls-iminiporttopology.md) | The IMiniportTopology interface is the primary interface of a Topology miniport driver. |
| [IMiniportWaveCyclic](nn-portcls-iminiportwavecyclic.md) | The IMiniportWaveCyclic interface is the primary interface that is exposed by the miniport driver for a WaveCyclic audio device. |
| [IMiniportWaveCyclicStream](nn-portcls-iminiportwavecyclicstream.md) | The IMiniportWaveCyclicStream interface represents the wave stream that flows through a pin on a WaveCyclic filter. |
| [IMiniportWavePci](nn-portcls-iminiportwavepci.md) | The IMiniportWavePci interface is the primary interface that is exposed by the miniport driver for a WavePci audio device. |
| [IMiniportWavePciStream](nn-portcls-iminiportwavepcistream.md) | The IMiniportWavePciStream interface represents the wave stream that flows through a pin on a WavePci filter. |
| [IMiniportWaveRT](nn-portcls-iminiportwavert.md) | The IMiniportWaveRT interface is the primary interface that is exposed by the miniport driver for a WaveRT audio device. |
| [IMiniportWaveRTInputStream](nn-portcls-iminiportwavertinputstream.md) | The IMiniportWaveRTInputStream interface represents the input wave stream that flows through a pin on the KS filter that wraps a WaveRT rendering or capture device. IMiniportWaveRTInputStream inherits from the IUnknown interface. |
| [IMiniportWaveRTOutputStream](nn-portcls-iminiportwavertoutputstream.md) | The IMiniportWaveRTOutputStream interface represents the output wave stream. IMiniportWaveRTOutputStream inherits from the IUnknown interface. |
| [IMiniportWaveRTStream](nn-portcls-iminiportwavertstream.md) | The IMiniportWaveRTStream interface represents the wave stream that flows through a pin on the KS filter that wraps a WaveRT rendering or capture device. |
| [IMiniportWaveRTStreamNotification](nn-portcls-iminiportwavertstreamnotification.md) | The IMiniportWaveRTStreamNotification interface is supported in Windows Vista and later Windows operating systems, and it augments the IMiniportWaveRTStream interface, providing additional methods to facilitate DMA driver event notifications. |
| [IMusicTechnology](nn-portcls-imusictechnology.md) | The IMusicTechnology interface is used to change the music technology GUIDs that are specified in the data range descriptors for the pins belonging to a MIDI or DMus miniport driver. |
| [IPinCount](nn-portcls-ipincount.md) | The IPinCount interface provides a means for the miniport driver to monitor and manipulate its pin counts dynamically as pins are instantiated and closed. |
| [IPinName](nn-portcls-ipinname.md) | In Windows 7 and later operating systems, the IPinName interface is used by miniport drivers to report and update the names of audio endpoints. |
| [IPort](nn-portcls-iport.md) | The IPort interface is the generic interface for audio port drivers. All audio port drivers expose IPort as part of their lower edge. The adapter driver calls the initialization method on this interface. IPort inherits from the IUnknown interface. |
| [IPortClsEtwHelper](nn-portcls-iportclsetwhelper.md) | The IPortClsEtwHelper interface allows an audio miniport driver to access the Event Tracing for Windows (ETW) helper functions. |
| [IPortClsNotifications](nn-portcls-iportclsnotifications.md) | An interface implemented by ports to provide notification helpers to miniports to support audio module communication. |
| [IPortClsPnp](nn-portcls-iportclspnp.md) | IPortClsPnp is the PnP management interface that the port class driver (PortCls) exposes to the adapter. |
| [IPortClsPower](nn-portcls-iportclspower.md) | The IPortClsPower interface is supported in Windows Vista and later versions of Windows. IPortClsPower is the power management interface that the port class driver (PortCls) exposes to the adapter. |
| [IPortClsRuntimePower](nn-portcls-iportclsruntimepower.md) | IPortClsRuntimePower is the interface that the port class driver (PortCls) uses for accessing the runtime power management capabilities of the audio adapter. |
| [IPortClsStreamResourceManager](nn-portcls-iportclsstreamresourcemanager.md) | IPortClsStreamResourceManager is used to manage the registration of audio stream resources. |
| [IPortClsStreamResourceManager2](nn-portcls-iportclsstreamresourcemanager2.md) | IPortClsStreamResourceManager2 is used to manage the registration of audio stream resources. |
| [IPortClsVersion](nn-portcls-iportclsversion.md) | The IPortClsVersion interface is used by a miniport driver to identify the version of the Windows operating system that the driver is running on. The port driver implements this interface and exposes it to the miniport driver. |
| [IPortEvents](nn-portcls-iportevents.md) | The IPortEvents interface is used by miniport drivers to notify clients of hardware events. |
| [IPortMidi](nn-portcls-iportmidi.md) | The IPortMidi interface is the MIDI port driver's primary interface. |
| [IPortTopology](nn-portcls-iporttopology.md) | The IPortTopology interface provides generic port driver support to a topology miniport driver. |
| [IPortWaveCyclic](nn-portcls-iportwavecyclic.md) | The IPortWaveCyclic interface is the WaveCyclic port driver's primary interface. |
| [IPortWavePci](nn-portcls-iportwavepci.md) | The IPortWavePci interface is the WavePci port driver's primary interface. |
| [IPortWavePciStream](nn-portcls-iportwavepcistream.md) | The IPortWavePciStream interface is the stream-associated callback interface that provides mapping services to WavePci miniport stream objects. |
| [IPortWaveRT](nn-portcls-iportwavert.md) | The IPortWaveRT interface is supported in Windows Vista and later operating systems and it is the main interface that the WaveRT port driver exposes to the adapter driver that implements the WaveRT miniport driver object. |
| [IPortWaveRTStream](nn-portcls-iportwavertstream.md) | The IPortWaveRTStream interface is supported in Windows Vista and later operating systems, and it is a stream-specific interface that provides helper methods for use by the WaveRT miniport driver. |
| [IPortWMIRegistration](nn-portcls-iportwmiregistration.md) | The IPortWMIRegistration interface is provided in Windows 7 and later versions of Windows. This interface allows the miniport driver to coordinate Event Tracing for Windows (ETW) registration between PortCls and the miniport driver. |
| [IPowerNotify](nn-portcls-ipowernotify.md) | The IPowerNotify interface is an optional interface that miniport drivers can expose if they require advance notification of impending power-state changes. |
| [IPreFetchOffset](nn-portcls-iprefetchoffset.md) | The IPreFetchOffset interface controls the prefetch offset, which is the number of bytes separating the play and write cursors in a DirectSound output stream. |
| [IRegistryKey](nn-portcls-iregistrykey.md) | The IRegistryKey interface provides an abstraction of a registry key that a miniport driver can use to access the key and its subkeys. |
| [IResourceList](nn-portcls-iresourcelist.md) | The IResourceList interface provides an abstraction of a configuration resource list, which is a list of the system hardware resources that the Plug and Play manager assigns to a device at startup time. |
| [IServiceGroup](nn-portcls-iservicegroup.md) | The IServiceGroup interface encapsulates a group of objects that all require notification of the same service request. |
| [IServiceSink](nn-portcls-iservicesink.md) | The IServiceSink interface encapsulates handling of a service request. |
| [IUnregisterPhysicalConnection](nn-portcls-iunregisterphysicalconnection.md) | The IUnregisterPhysicalConnection interface implements three methods to remove a registered physical connection. |
| [IUnregisterSubdevice](nn-portcls-iunregistersubdevice.md) | The IUnregisterSubdevice interface implements a method to remove a registered subdevice. |



## Functions
| Title | Description |
| ---- |:---- |
| [PCPFNEVENT_HANDLER](nc-portcls-pcpfnevent_handler.md) | An EventHandler routine processes event requests. |
| [PcAddAdapterDevice](nf-portcls-pcaddadapterdevice.md) | The PcAddAdapterDevice function adds an adapter device to the WDM device stack. |
| [PcAddContentHandlers](nf-portcls-pcaddcontenthandlers.md) | The PcAddContentHandlers function provides the system with a list of functions that handle protected content. |
| [PcAddStreamResource](nf-portcls-pcaddstreamresource.md) | PcAddStreamResource adds a stream resource. |
| [PcCompleteIrp](nf-portcls-pccompleteirp.md) | The PcCompleteIrp function completes an IRP that was previously marked as pending. |
| [PcCompletePendingPropertyRequest](nf-portcls-pccompletependingpropertyrequest.md) | The PcCompletePendingPropertyRequest function is called to complete a pending property request. |
| [PcCreateContentMixed](nf-portcls-pccreatecontentmixed.md) | The PcCreateContentMixed function computes the DRM content rights for a composite stream containing mixed content from some number of KS audio streams. |
| [PcDestroyContent](nf-portcls-pcdestroycontent.md) | The PcDestroyContent function deletes a DRM content ID that was created by PcCreateContentMixed. Note that this function call is identical in operation to the DrmDestroyContent function, and its parameter definitions and return value are also identical. |
| [PcDispatchIrp](nf-portcls-pcdispatchirp.md) | The PcDispatchIrp function dispatches an IRP to the PortCls system driver's default handler. |
| [PcForwardContentToDeviceObject](nf-portcls-pcforwardcontenttodeviceobject.md) | The PcForwardContentToDeviceObject function accepts a device object representing a device to which the caller intends to forward protected content. |
| [PcForwardContentToFileObject](nf-portcls-pcforwardcontenttofileobject.md) | The PcForwardContentToFileObject function is obsolete and is maintained only to support existing drivers. |
| [PcForwardContentToInterface](nf-portcls-pcforwardcontenttointerface.md) | The PcForwardContentToInterface function accepts a pointer to the COM interface of an object to which the caller intends to forward protected content. |
| [PcForwardIrpSynchronous](nf-portcls-pcforwardirpsynchronous.md) | The PcForwardIrpSynchronous function is used by IRP handlers to forward Plug and Play IRPs to the physical device object (PDO). |
| [PcGetContentRights](nf-portcls-pcgetcontentrights.md) | The PcGetContentRights function retrieves the DRM content rights assigned to a DRM content ID. Note that this function call is identical in operation to the DrmGetContentRights function, and its parameter definitions and return value are also identical. |
| [PcGetDeviceProperty](nf-portcls-pcgetdeviceproperty.md) | The PcGetDeviceProperty function returns the requested device property from the registry. |
| [PcGetPhysicalDeviceObject](nf-portcls-pcgetphysicaldeviceobject.md) | The PcGetPhysicalDeviceObject function enables audio miniport drivers to retrieve the underlying physical device object of the audio device. |
| [PcGetTimeInterval](nf-portcls-pcgettimeinterval.md) | The PcGetTimeInterval function returns the time elapsed since a specified time. Time is measured in 100-nanosecond units. |
| [PcInitializeAdapterDriver](nf-portcls-pcinitializeadapterdriver.md) | The PcInitializeAdapterDriver function binds an adapter driver to the PortCls system driver. |
| [PcNewDmaChannel](nf-portcls-pcnewdmachannel.md) | The PcNewDmaChannel function creates a new DMA-channel object. This function is obsolete; for more information, see the following comments. |
| [PcNewInterruptSync](nf-portcls-pcnewinterruptsync.md) | The PcNewInterruptSync function creates and initializes an interrupt-synchronization object. |
| [PcNewMiniport](nf-portcls-pcnewminiport.md) | The PcNewMiniport function creates an instance of one of the system-supplied miniport drivers that are built into the PortCls system driver, portcls.sys. |
| [PcNewPort](nf-portcls-pcnewport.md) | The PcNewPort function creates a new system-supplied port-driver object, whose interface (derived from base class IPort) is specified by a class ID. |
| [PcNewRegistryKey](nf-portcls-pcnewregistrykey.md) | The PcNewRegistryKey function opens or creates a new registry key and creates an IRegistryKey object to represent the key. The caller accesses the key through this object. |
| [PcNewResourceList](nf-portcls-pcnewresourcelist.md) | The PcNewResourceList function creates and initializes a resource list. |
| [PcNewResourceSublist](nf-portcls-pcnewresourcesublist.md) | The PcNewResourceSublist function creates and initializes an empty resource list that is derived from another resource list. |
| [PcNewServiceGroup](nf-portcls-pcnewservicegroup.md) | The PcNewServiceGroup function creates and initializes a service group. |
| [PcRegisterAdapterPnpManagement](nf-portcls-pcregisteradapterpnpmanagement.md) | The PcRegisterAdapterPnpManagement function registers the adapter's PnP-management interface with the PortCls system driver. It is used to support PnP rebalance. |
| [PcRegisterAdapterPowerManagement](nf-portcls-pcregisteradapterpowermanagement.md) | The PcRegisterAdapterPowerManagement function registers the adapter's power-management interface with the PortCls system driver. |
| [PcRegisterIoTimeout](nf-portcls-pcregisteriotimeout.md) | The PcRegisterIoTimeout function registers a driver-supplied I/O-timer callback routine for a specified device object. |
| [PcRegisterPhysicalConnection](nf-portcls-pcregisterphysicalconnection.md) | The PcRegisterPhysicalConnection function registers a physical connection between two audio adapter filters that are instantiated by the same adapter driver. |
| [PcRegisterPhysicalConnectionFromExternal](nf-portcls-pcregisterphysicalconnectionfromexternal.md) | The PcRegisterPhysicalConnectionFromExternal function registers a physical connection to an audio adapter filter from an external audio adapter filter. |
| [PcRegisterPhysicalConnectionToExternal](nf-portcls-pcregisterphysicalconnectiontoexternal.md) | The PcRegisterPhysicalConnectionToExternal function registers a physical connection from an audio adapter filter to an external audio adapter filter. |
| [PcRegisterSubdevice](nf-portcls-pcregistersubdevice.md) | The PcRegisterSubdevice function registers a subdevice to make it available for use by clients. |
| [PcRemoveStreamResource](nf-portcls-pcremovestreamresource.md) | PcRemoveStreamResource removes an existing stream resource. |
| [PcRequestNewPowerState](nf-portcls-pcrequestnewpowerstate.md) | The PcRequestNewPowerState function is used to request a new power state for the device. This function is typically not needed by adapter drivers but can occasionally be useful in working around some kinds of hardware problems. |
| [PcUnregisterAdapterPnpManagement](nf-portcls-pcunregisteradapterpnpmanagement.md) | The PcUnregisterAdapterPnpManagement function unregisters the audio adapter's PnP management interface from the PortCls class driver. It is used to support PnP rebalance. |
| [PcUnregisterAdapterPowerManagement](nf-portcls-pcunregisteradapterpowermanagement.md) | The PcUnregisterAdapterPowerManagement function unregisters the audio adapter's power management interface from the PortCls class driver. The PcUnregisterAdapterPowerManagement function is available in Windows 7 and later versions of Windows. |
| [PcUnregisterIoTimeout](nf-portcls-pcunregisteriotimeout.md) | The PcUnregisterIoTimeout function unregisters a driver-supplied I/O-timer callback routine for a specified device object. |



## Structures
| Title | Description |
| ---- |:---- |
| [_PCEVENT_REQUEST](ns-portcls-_pcevent_request.md) | The PCEVENT_REQUEST structure specifies an event request. |
| [_PCMETHOD_REQUEST](ns-portcls-_pcmethod_request.md) | The PCMETHOD_REQUEST structure specifies a method request. |
| [_PCNOTIFICATION_BUFFER](ns-portcls-_pcnotification_buffer.md) | The notification buffer used by IPortClsNotifications. |
| [_PCPROPERTY_REQUEST](ns-portcls-_pcproperty_request.md) | The PCPROPERTY_REQUEST structure specifies a property request. |
| [_PCSTREAMRESOURCE_DESCRIPTOR](ns-portcls-_pcstreamresource_descriptor.md) | PCSTREAMRESOURCE_DESCRIPTOR defines the stream resource. Use PCSTREAMRESOURCE_DESCRIPTOR_INIT to correctly initialize this structure. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_PC_EXIT_LATENCY](ne-portcls-_pc_exit_latency.md) | This topic discusses the PC_EXIT_LATENCY enum, and describes its members. The latency times map to specific maximum times in which the device must be able to exit its sleep state and enter the fully functional state (D0). |
| [_PcStreamResourceType](ne-portcls-_pcstreamresourcetype.md) | This topic discusses the PcStreamResourceType enum, and describes its members. The PcStreamResourceType enum is used to define the type of resources used for specific audio streaming. |
| [eChannelTargetType](ne-portcls-echanneltargettype.md) | The eChannelTargetType enumeration defines constants that specify a type of node (target) in a given channel. |
| [eEngineFormatType](ne-portcls-eengineformattype.md) | The eEngineFormatType enumeration defines constants that specify the audio data type supported by the audio engine. |
| [EPcMiniportEngineEvent](ne-portcls-epcminiportengineevent.md) | This topic introduces the EPcMiniportEngineEvent enum, and describes the parameters that provide additional information when the miniport driver reports a glitching error. |
| [PC_REBALANCE_TYPE](ne-portcls-pc_rebalance_type.md) | The PC_REBALANCE_TYPE enum describes the type of support for rebalancing. |