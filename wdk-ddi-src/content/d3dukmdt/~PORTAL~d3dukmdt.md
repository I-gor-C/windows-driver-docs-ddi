# D3Dukmdt.h header


This header is used by unknown technology.

D3Dukmdt.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [D3DDDIARG_CREATERESOURCE structure](ns-d3dukmdt--d3dddiarg-createresource.md) | The D3DDDIARG_CREATERESOURCE structure contains information for creating a resource. |
| [D3DDDIARG_CREATERESOURCE2 structure](ns-d3dukmdt--d3dddiarg-createresource2.md) | Contains information for creating a resource. Used by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [D3DDDICB_DESTROYALLOCATION2FLAGS structure](ns-d3dukmdt--d3dddicb-destroyallocation2flags.md) | The D3DDDICB_DESTROYALLOCATION2FLAGS structure is used with the D3DKMT_DESTROYALLOCATION2 structure to describe parameters for releasing allocations with D3DKMTDestroyAllocation2.D3DDDICB_DESTROYALLOCATION2FLAGS structure is used with the D3DKMT_DESTROYALLOCATION2 structure to describe parameters for releasing allocations with D3DKMTDestroyAllocation2. |
| [D3DDDICB_LOCK2FLAGS structure](ns-d3dukmdt--d3dddicb-lock2flags.md) | D3DDDICB_LOCK2FLAGS is used by the Lock2 kernel function to determine how an allocation is locked. |
| [D3DDDICB_LOCKFLAGS structure](ns-d3dukmdt--d3dddicb-lockflags.md) | The D3DDDICB_LOCKFLAGS structure identifies how to lock an allocation. |
| [D3DDDICB_SIGNALFLAGS structure](ns-d3dukmdt--d3dddicb-signalflags.md) | The D3DDDICB_SIGNALFLAGS structure describes signaling behavior in a call to the pfnSignalSynchronizationObjectCb or pfnSignalSynchronizationObject2Cb functions. |
| [D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE structure](ns-d3dukmdt--d3dddigpuvirtualaddress-protection-type.md) | D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE specifies the protection on the graphics processing unit (GPU) virtual address that is mapped. |
| [D3DDDIRECT structure](ns-d3dukmdt--d3dddirect.md) | The D3DDDIRECT structure defines a rectangle by the coordinates of its upper-left and lower-right corners. |
| [D3DDDI_ALLOCATIONINFO structure](ns-d3dukmdt--d3dddi-allocationinfo.md) | The D3DDDI_ALLOCATIONINFO structure describes an allocation. |
| [D3DDDI_ALLOCATIONLIST structure](ns-d3dukmdt--d3dddi-allocationlist.md) | The D3DDDI_ALLOCATIONLIST structure describes information about an allocation specification that is used in direct memory access (DMA) buffering. |
| [D3DDDI_CREATECONTEXTFLAGS structure](ns-d3dukmdt--d3dddi-createcontextflags.md) | The D3DDDI_CREATECONTEXTFLAGS structure describes how to create a context in a call to the pfnCreateContextCb function. |
| [D3DDDI_CREATEHWCONTEXTFLAGS structure](ns-d3dukmdt--d3dddi-createhwcontextflags.md) | A structure used to create hardware context flags. |
| [D3DDDI_CREATEHWQUEUEFLAGS structure](ns-d3dukmdt--d3dddi-createhwqueueflags.md) | A structure used to create hardware queue flags. |
| [D3DDDI_DESTROYPAGINGQUEUE structure](ns-d3dukmdt-d3dddi-destroypagingqueue.md) | D3DDDI_DESTROYPAGINGQUEUE is used with pfnDestroyPagingQueueCb and D3DKMTDestroyPagingQueue to wait for a paging queue to finish all operations queued to it and destroy it along with the associated sync object. |
| [D3DDDI_DXGI_RGB structure](ns-d3dukmdt-d3dddi-dxgi-rgb.md) | The D3DDDI_DXGI_RGB structure contains information to describe a gamma function. |
| [D3DDDI_ESCAPEFLAGS structure](ns-d3dukmdt--d3dddi-escapeflags.md) | The D3DDDI_ESCAPEFLAGS structure identifies how the user-mode display driver shares information with the display miniport driver. |
| [D3DDDI_EVICT_FLAGS structure](ns-d3dukmdt-d3dddi-evict-flags.md) | D3DDDI_EVICT_FLAGS specifies the eviction behavior. |
| [D3DDDI_GAMMA_RAMP_DXGI_1 structure](ns-d3dukmdt--d3dddi-gamma-ramp-dxgi-1.md) | The D3DDDI_GAMMA_RAMP_DXGI_1 structure describes a gamma function. |
| [D3DDDI_GAMMA_RAMP_RGB256x3x16 structure](ns-d3dukmdt--d3dddi-gamma-ramp-rgb256x3x16.md) | The D3DDDI_GAMMA_RAMP_RGB256x3x16 structure contains a gamma lookup table. |
| [D3DDDI_GETRESOURCEPRESENTPRIVATEDRIVERDATA structure](ns-d3dukmdt--d3dddi-getresourcepresentprivatedriverdata.md) | D3DDDI_GETRESOURCEPRESENTPRIVATEDRIVERDATA is used with pfnGetResourcePresentPrivateDriverDataCb to query the resource private data, which is associated with the resource during Present. |
| [D3DDDI_HDR_METADATA_HDR10 structure](ns-d3dukmdt--d3dddi-hdr-metadata-hdr10.md) | Describes the metadata for HDR10. |
| [D3DDDI_KERNELOVERLAYINFO structure](ns-d3dukmdt--d3dddi-kerneloverlayinfo.md) | The D3DDDI_KERNELOVERLAYINFO structure describes information for a kernel-mode overlay object. |
| [D3DDDI_MAKERESIDENT structure](ns-d3dukmdt-d3dddi-makeresident.md) | D3DDDI_MAKERESIDENT is used with MakeResident (pfnMakeResidentCb or D3DKMTMakeResident) to instruct the OS to add a resource to the device residency list and increment the residency reference count on this allocation. |
| [D3DDDI_MAKERESIDENT_FLAGS structure](ns-d3dukmdt-d3dddi-makeresident-flags.md) | D3DDDI_MAKERESIDENT_FLAGS is used with MakeResident (pfnMakeResidentCb or D3DKMTMakeResident) to instruct the OS to add a resource to the device residency list and increment the residency reference count on this allocation. |
| [D3DDDI_MAPGPUVIRTUALADDRESS structure](ns-d3dukmdt-d3dddi-mapgpuvirtualaddress.md) | D3DDDI_MAPGPUVIRTUALADDRESS is used with pfnMapGpuVirtualAddressCb to map a graphics processing unit (GPU) virtual address ranges to a specific allocation range or to put it to the Invalid or Zero state. |
| [D3DDDI_MULTISAMPLINGMETHOD structure](ns-d3dukmdt--d3dddi-multisamplingmethod.md) | The D3DDDI_MULTISAMPLINGMETHOD structure describes a multiple-sampling method. |
| [D3DDDI_OPENALLOCATIONINFO structure](ns-d3dukmdt--d3dddi-openallocationinfo.md) | The D3DDDI_OPENALLOCATIONINFO structure describes an allocation to be opened. |
| [D3DDDI_OPENALLOCATIONINFO2 structure](ns-d3dukmdt--d3dddi-openallocationinfo2.md) | Reserved for system use. Do not use in your driver. |
| [D3DDDI_PATCHLOCATIONLIST structure](ns-d3dukmdt--d3dddi-patchlocationlist.md) | The D3DDDI_PATCHLOCATIONLIST structure describes the location of an allocation to patch (that is, assign a physical address to the allocation). |
| [D3DDDI_RATIONAL structure](ns-d3dukmdt--d3dddi-rational.md) | The D3DDDI_RATIONAL structure describes a fractional value that represents vertical and horizontal frequencies of a video mode (that is, vertical sync and horizontal sync). |
| [D3DDDI_RESERVEGPUVIRTUALADDRESS structure](ns-d3dukmdt-d3dddi-reservegpuvirtualaddress.md) | D3DDDI_RESERVEGPUVIRTUALADDRESS is used with pfnReserveGpuVirtualAddressCb to reserve an address range in the graphics processing unit (GPU) virtual address space of the current process. |
| [D3DDDI_RESOURCEFLAGS structure](ns-d3dukmdt--d3dddi-resourceflags.md) | The D3DDDI_RESOURCEFLAGS structure identifies the type of resources to create in a call to the driver's CreateResource function. |
| [D3DDDI_RESOURCEFLAGS2 structure](ns-d3dukmdt--d3dddi-resourceflags2.md) | Identifies the type of resource to create in a call to the driver's CreateResource2 function. |
| [D3DDDI_SURFACEINFO structure](ns-d3dukmdt--d3dddi-surfaceinfo.md) | The D3DDDI_SURFACEINFO structure describes a resource type, such as a surface. |
| [D3DDDI_SYNCHRONIZATIONOBJECTINFO structure](ns-d3dukmdt--d3dddi-synchronizationobjectinfo.md) | The D3DDDI_SYNCHRONIZATIONOBJECTINFO structure contains information about a synchronization object. |
| [D3DDDI_SYNCHRONIZATIONOBJECTINFO2 structure](ns-d3dukmdt--d3dddi-synchronizationobjectinfo2.md) | The D3DDDI_SYNCHRONIZATIONOBJECTINFO2 structure contains information about a second-generation synchronization object. |
| [D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS structure](ns-d3dukmdt--d3dddi-synchronizationobject-flags.md) | Identifies attributes of a synchronization object. |
| [D3DDDI_TRIMRESIDENCYSET_FLAGS structure](ns-d3dukmdt-d3dddi-trimresidencyset-flags.md) | D3DDDI_TRIMRESIDENCYSET_FLAGS is used with pfnTrimResidencySet to trim the residency list for a given device. |
| [D3DDDI_UPDATEALLOCPROPERTY structure](ns-d3dukmdt-d3dddi-updateallocproperty.md) | D3DDDI_UPDATEALLOCPROPERTY describes the parameters needed to update an allocation. |
| [D3DDDI_UPDATEALLOCPROPERTY_FLAGS structure](ns-d3dukmdt-d3dddi-updateallocproperty-flags.md) | The D3DDDI_UPDATEALLOCPROPERTY_FLAGS structure identifies how to update a property in an allocation. |
| [D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION structure](ns-d3dukmdt--d3dddi-updategpuvirtualaddress-operation.md) | D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION describes a virtual address update operation. |
| [D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS structure](ns-d3dukmdt--d3dddi-waitforsynchronizationobjectfromcpu-flags.md) | D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS describes the type of input synchronization objects to wait for. |
| [DXGKVGPU_ESCAPE_HEAD structure](ns-d3dukmdt--dxgkvgpu-escape-head.md) | A structure describing the escape head. |
| [DXGKVGPU_ESCAPE_INITIALIZE structure](ns-d3dukmdt--dxgkvgpu-escape-initialize.md) | Used to initialize an escape. |
| [DXGKVGPU_ESCAPE_POWERTRANSITIONCOMPLETE structure](ns-d3dukmdt--dxgkvgpu-escape-powertransitioncomplete.md) | Indicates that a power transition has completed. |
| [DXGKVGPU_ESCAPE_READ_PCI_CONFIG structure](ns-d3dukmdt--dxgkvgpu-escape-read-pci-config.md) | A structure used to read the PCI config for an escape. |
| [DXGKVGPU_ESCAPE_READ_VGPU_TYPE structure](ns-d3dukmdt--dxgkvgpu-escape-read-vgpu-type.md) | A structure used to read the VGPU type of an escape. |
| [DXGKVGPU_ESCAPE_RELEASE structure](ns-d3dukmdt--dxgkvgpu-escape-release.md) | Indicates that an escape has been released. |
| [DXGKVGPU_ESCAPE_WRITE_PCI_CONFIG structure](ns-d3dukmdt--dxgkvgpu-escape-write-pci-config.md) | Used to write to the PCI config space. |
| [DXGK_MIRACAST_CHUNK_ID structure](ns-d3dukmdt-dxgk-miracast-chunk-id.md) | Stores info that identifies a wireless display (Miracast) encode chunk. |
| [DXGK_MIRACAST_CHUNK_INFO structure](ns-d3dukmdt-dxgk-miracast-chunk-info.md) | Contains info about a specified wireless display (Miracast) encode chunk. |
| [DXGK_PTE structure](ns-d3dukmdt--dxgk-pte.md) | A page table entry (PTE) provides a physical address of a page and other attributes. The exact format of PTE depends on hardware implementation. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [D3DDDIFORMAT enumeration](ne-d3dukmdt--d3dddiformat.md) | The D3DDDIFORMAT enumeration type contains values that identify surface formats. |
| [D3DDDIMULTISAMPLE_TYPE enumeration](ne-d3dukmdt--d3dddimultisample-type.md) | The D3DDDIMULTISAMPLE_TYPE enumeration defines the levels of full-scene multisampling that the device can apply. |
| [D3DDDI_COLOR_SPACE_TYPE enumeration](ne-d3dukmdt-d3dddi-color-space-type.md) | Defines stream color space information. |
| [D3DDDI_FLIPINTERVAL_TYPE enumeration](ne-d3dukmdt-d3dddi-flipinterval-type.md) | The D3DDDI_FLIPINTERVAL_TYPE enumeration type contains values that identify the type of flip that occurs in present operations. |
| [D3DDDI_GAMMARAMP_TYPE enumeration](ne-d3dukmdt--d3dddi-gammaramp-type.md) | The D3DDDI_GAMMARAMP_TYPE enumeration indicates the type of gamma ramp used in a video present path. |
| [D3DDDI_HDR_METADATA_TYPE enumeration](ne-d3dukmdt--d3dddi-hdr-metadata-type.md) | Defines the format of HDR metadata. |
| [D3DDDI_OFFER_PRIORITY enumeration](ne-d3dukmdt--d3dddi-offer-priority.md) | Indicates the importance of video memory resources that the user-mode display driver offers for reuse. |
| [D3DDDI_PAGINGQUEUE_PRIORITY enumeration](ne-d3dukmdt-d3dddi-pagingqueue-priority.md) | The D3DDDI_PAGINGQUEUE_PRIORITY enumeration indicates the scheduling priority relative to other paging queues on a device. |
| [D3DDDI_POOL enumeration](ne-d3dukmdt--d3dddi-pool.md) | The D3DDDI_POOL enumeration type contains values that identify particular types of memory pool. |
| [D3DDDI_ROTATION enumeration](ne-d3dukmdt--d3dddi-rotation.md) | The D3DDDI_ROTATION enumeration type contains values that identify the orientation of a resource. |
| [D3DDDI_SCANLINEORDERING enumeration](ne-d3dukmdt-d3dddi-scanlineordering.md) | The D3DDDI_SCANLINEORDERING enumeration type contains values that identify how the scan lines are drawn on a surface. |
| [D3DDDI_SYNCHRONIZATIONOBJECT_TYPE enumeration](ne-d3dukmdt--d3dddi-synchronizationobject-type.md) | The D3DDDI_SYNCHRONIZATIONOBJECT_TYPE enumeration indicates the type of synchronization object. |
| [D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION_TYPE enumeration](ne-d3dukmdt--d3dddi-updategpuvirtualaddress-operation-type.md) | D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION_TYPE describes the details of the virtual address update operation being performed. |
| [D3DDDI_VIDEO_SIGNAL_SCANLINE_ORDERING enumeration](ne-d3dukmdt--d3dddi-video-signal-scanline-ordering.md) | The D3DDDI_VIDEO_SIGNAL_SCANLINE_ORDERING enumeration is used to indicate the scan line ordering of a video output signal. |
| [DXGKVGPU_ESCAPE_TYPE enumeration](ne-d3dukmdt--dxgkvgpu-escape-type.md) | An enum that holds information about the escape type. |
| [DXGK_MIRACAST_CHUNK_TYPE enumeration](ne-d3dukmdt--dxgk-miracast-chunk-type.md) | Specifies the types of wireless display (Miracast) chunk info that is to be processed. |
| [DXGK_PTE_PAGE_SIZE enumeration](ne-d3dukmdt--dxgk-pte-page-size.md) | The DXGK_PTE_PAGE_SIZE enumeration is used by DXGK_PTE to indicate the size of lower page level pages. |
